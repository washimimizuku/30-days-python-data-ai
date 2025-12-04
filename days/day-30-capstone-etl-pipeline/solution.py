"""
Day 30: Capstone Project - ETL Pipeline - Solution
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import os

print("="*70)
print(" "*15 + "DAY 30: CAPSTONE ETL PIPELINE")
print("="*70)
print()

class ETLPipeline:
    """Complete ETL Pipeline for Sensor Data"""
    
    def __init__(self, name: str = "Sensor Data Pipeline"):
        self.name = name
        self.raw_data = []
        self.cleaned_data = None
        self.aggregated_data = None
        self.results = {}
        self.start_time = None
        self.end_time = None
    
    def extract(self) -> None:
        """Extract data from multiple sources"""
        print("STEP 1: EXTRACT")
        print("-" * 70)
        
        # Source 1: CSV file
        print("  Extracting from CSV...")
        csv_data = self._create_csv_source()
        df_csv = pd.read_csv("data/raw/sensor_data.csv")
        print(f"    ✓ Loaded {len(df_csv)} records from CSV")
        
        # Source 2: JSON file
        print("  Extracting from JSON...")
        json_data = self._create_json_source()
        with open("data/raw/sensor_data.json", "r") as f:
            data_json = json.load(f)
        df_json = pd.DataFrame(data_json)
        print(f"    ✓ Loaded {len(df_json)} records from JSON")
        
        # Source 3: Simulated API
        print("  Extracting from API...")
        df_api = self._extract_from_api()
        print(f"    ✓ Loaded {len(df_api)} records from API")
        
        # Combine all sources
        self.raw_data = pd.concat([df_csv, df_json, df_api], ignore_index=True)
        print(f"\n  Total records extracted: {len(self.raw_data)}")
        print()
    
    def transform(self) -> None:
        """Transform and clean data"""
        print("STEP 2: TRANSFORM")
        print("-" * 70)
        
        df = self.raw_data.copy()
        initial_count = len(df)
        
        # 1. Remove duplicates
        df = df.drop_duplicates()
        duplicates_removed = initial_count - len(df)
        print(f"  ✓ Removed {duplicates_removed} duplicates")
        
        # 2. Handle missing values
        missing_before = df.isnull().sum().sum()
        df = df.dropna(subset=['sensor_id', 'timestamp'])
        df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
        df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
        print(f"  ✓ Handled {missing_before} missing values")
        
        # 3. Data type conversion
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed')
        df['sensor_id'] = df['sensor_id'].astype(int)
        print(f"  ✓ Converted data types")
        
        # 4. Remove outliers
        for col in ['temperature', 'humidity']:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            df = df[
                (df[col] >= Q1 - 1.5 * IQR) &
                (df[col] <= Q3 + 1.5 * IQR)
            ]
        outliers_removed = len(self.raw_data) - len(df)
        print(f"  ✓ Removed {outliers_removed} outliers")
        
        # 5. Add derived columns
        df['date'] = df['timestamp'].dt.date
        df['hour'] = df['timestamp'].dt.hour
        df['day_of_week'] = df['timestamp'].dt.day_name()
        df['temp_category'] = pd.cut(
            df['temperature'],
            bins=[-np.inf, 20, 25, 30, np.inf],
            labels=['Cold', 'Cool', 'Warm', 'Hot']
        )
        print(f"  ✓ Added derived columns")
        
        self.cleaned_data = df
        print(f"\n  Final record count: {len(df)}")
        print()
    
    def validate(self) -> bool:
        """Validate data quality"""
        print("STEP 3: VALIDATE")
        print("-" * 70)
        
        df = self.cleaned_data
        issues = []
        
        # Check for required columns
        required_cols = ['sensor_id', 'timestamp', 'temperature', 'humidity']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            issues.append(f"Missing columns: {missing_cols}")
        
        # Check value ranges
        if (df['temperature'] < -50).any() or (df['temperature'] > 50).any():
            issues.append("Temperature out of valid range")
        
        if (df['humidity'] < 0).any() or (df['humidity'] > 100).any():
            issues.append("Humidity out of valid range")
        
        # Check for nulls
        null_counts = df[required_cols].isnull().sum()
        if null_counts.any():
            issues.append(f"Null values found: {null_counts[null_counts > 0].to_dict()}")
        
        if issues:
            print("  ✗ Validation failed:")
            for issue in issues:
                print(f"    - {issue}")
            return False
        else:
            print("  ✓ All validation checks passed")
            print(f"    - {len(df)} records validated")
            print(f"    - {len(df.columns)} columns present")
            print(f"    - No data quality issues found")
            print()
            return True
    
    def aggregate(self) -> None:
        """Aggregate and analyze data"""
        print("STEP 4: AGGREGATE")
        print("-" * 70)
        
        df = self.cleaned_data
        
        # Overall statistics
        overall_stats = {
            'total_records': len(df),
            'unique_sensors': df['sensor_id'].nunique(),
            'date_range': {
                'start': df['timestamp'].min().isoformat(),
                'end': df['timestamp'].max().isoformat()
            },
            'temperature': {
                'mean': float(df['temperature'].mean()),
                'std': float(df['temperature'].std()),
                'min': float(df['temperature'].min()),
                'max': float(df['temperature'].max())
            },
            'humidity': {
                'mean': float(df['humidity'].mean()),
                'std': float(df['humidity'].std()),
                'min': float(df['humidity'].min()),
                'max': float(df['humidity'].max())
            }
        }
        
        # By sensor
        by_sensor = df.groupby('sensor_id').agg({
            'temperature': ['count', 'mean', 'std'],
            'humidity': ['mean', 'std']
        }).round(2)
        
        # Convert to JSON-serializable format
        by_sensor_dict = {}
        for sensor_id in by_sensor.index:
            by_sensor_dict[str(sensor_id)] = {
                'temperature_count': int(by_sensor.loc[sensor_id, ('temperature', 'count')]),
                'temperature_mean': float(by_sensor.loc[sensor_id, ('temperature', 'mean')]),
                'temperature_std': float(by_sensor.loc[sensor_id, ('temperature', 'std')]),
                'humidity_mean': float(by_sensor.loc[sensor_id, ('humidity', 'mean')]),
                'humidity_std': float(by_sensor.loc[sensor_id, ('humidity', 'std')])
            }
        
        # By hour
        by_hour = df.groupby('hour').agg({
            'temperature': 'mean',
            'humidity': 'mean'
        }).round(2)
        
        # By category
        by_category = df['temp_category'].value_counts().to_dict()
        
        self.aggregated_data = {
            'overall': overall_stats,
            'by_sensor': by_sensor_dict,
            'by_hour': {str(k): v for k, v in by_hour.to_dict('index').items()},
            'by_category': by_category
        }
        
        print(f"  ✓ Aggregated {len(df)} records")
        print(f"  ✓ Analyzed {df['sensor_id'].nunique()} sensors")
        print(f"  ✓ Generated statistics and insights")
        print()
    
    def load(self, output_dir: str = "data/processed") -> None:
        """Load data to output"""
        print("STEP 5: LOAD")
        print("-" * 70)
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Save cleaned data to CSV
        output_csv = f"{output_dir}/cleaned_sensor_data.csv"
        self.cleaned_data.to_csv(output_csv, index=False)
        print(f"  ✓ Saved cleaned data to {output_csv}")
        
        # Save aggregated results to JSON
        output_json = f"{output_dir}/analysis_results.json"
        with open(output_json, "w") as f:
            json.dump(self.aggregated_data, f, indent=2, default=str)
        print(f"  ✓ Saved analysis to {output_json}")
        
        # Generate summary report
        output_report = f"{output_dir}/pipeline_report.txt"
        self._generate_report(output_report)
        print(f"  ✓ Generated report: {output_report}")
        print()
    
    def run(self) -> None:
        """Run complete ETL pipeline"""
        self.start_time = datetime.now()
        
        print(f"\nStarting ETL Pipeline: {self.name}")
        print(f"Timestamp: {self.start_time}")
        print("="*70)
        print()
        
        try:
            self.extract()
            self.transform()
            
            if self.validate():
                self.aggregate()
                self.load()
                
                self.end_time = datetime.now()
                duration = (self.end_time - self.start_time).total_seconds()
                
                print("="*70)
                print(f"✓ PIPELINE COMPLETED SUCCESSFULLY")
                print(f"  Duration: {duration:.2f} seconds")
                print(f"  Records processed: {len(self.cleaned_data)}")
                print("="*70)
                
                # Cleanup
                self._cleanup()
            else:
                print("✗ Pipeline failed validation")
                
        except Exception as e:
            print(f"\n✗ Pipeline failed with error: {e}")
            raise
    
    def _create_csv_source(self) -> None:
        """Create sample CSV data"""
        np.random.seed(42)
        data = {
            'sensor_id': np.random.choice([101, 102, 103], 30),
            'timestamp': pd.date_range('2024-01-01', periods=30, freq='H'),
            'temperature': np.random.uniform(20, 30, 30),
            'humidity': np.random.uniform(40, 80, 30)
        }
        df = pd.DataFrame(data)
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv("data/raw/sensor_data.csv", index=False)
    
    def _create_json_source(self) -> None:
        """Create sample JSON data"""
        np.random.seed(43)
        data = [
            {
                'sensor_id': int(np.random.choice([101, 102, 103])),
                'timestamp': (datetime(2024, 1, 2) + timedelta(hours=i)).isoformat(),
                'temperature': float(np.random.uniform(20, 30)),
                'humidity': float(np.random.uniform(40, 80))
            }
            for i in range(20)
        ]
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/sensor_data.json", "w") as f:
            json.dump(data, f, indent=2)
    
    def _extract_from_api(self) -> pd.DataFrame:
        """Simulate API data extraction"""
        np.random.seed(44)
        data = {
            'sensor_id': np.random.choice([101, 102, 103], 25),
            'timestamp': pd.date_range('2024-01-03', periods=25, freq='H'),
            'temperature': np.random.uniform(20, 30, 25),
            'humidity': np.random.uniform(40, 80, 25)
        }
        return pd.DataFrame(data)
    
    def _generate_report(self, output_path: str) -> None:
        """Generate text report"""
        with open(output_path, "w") as f:
            f.write("="*70 + "\n")
            f.write(f"ETL Pipeline Report: {self.name}\n")
            f.write(f"Generated: {datetime.now()}\n")
            f.write("="*70 + "\n\n")
            
            stats = self.aggregated_data['overall']
            f.write(f"Total Records: {stats['total_records']}\n")
            f.write(f"Unique Sensors: {stats['unique_sensors']}\n")
            f.write(f"Date Range: {stats['date_range']['start']} to {stats['date_range']['end']}\n\n")
            
            f.write("Temperature Statistics:\n")
            f.write(f"  Mean: {stats['temperature']['mean']:.2f}°C\n")
            f.write(f"  Std: {stats['temperature']['std']:.2f}°C\n")
            f.write(f"  Range: {stats['temperature']['min']:.2f}°C to {stats['temperature']['max']:.2f}°C\n\n")
            
            f.write("Humidity Statistics:\n")
            f.write(f"  Mean: {stats['humidity']['mean']:.2f}%\n")
            f.write(f"  Std: {stats['humidity']['std']:.2f}%\n")
            f.write(f"  Range: {stats['humidity']['min']:.2f}% to {stats['humidity']['max']:.2f}%\n")
    
    def _cleanup(self) -> None:
        """Clean up temporary files"""
        # Clean up data files
        for folder in ["data/raw", "data/processed"]:
            if os.path.exists(folder):
                for f in os.listdir(folder):
                    if f != ".gitkeep":
                        filepath = os.path.join(folder, f)
                        if os.path.isfile(filepath):
                            os.remove(filepath)

# Run the pipeline
if __name__ == "__main__":
    pipeline = ETLPipeline("Sensor Data ETL Pipeline")
    pipeline.run()
    
    print("\n" + "="*70)
    print("🎉 CONGRATULATIONS! You've completed 30 Days of Python!")
    print("="*70)
    print("\nYou've learned:")
    print("  ✓ Python fundamentals")
    print("  ✓ Data structures and OOP")
    print("  ✓ File I/O and data processing")
    print("  ✓ NumPy and Pandas")
    print("  ✓ Data visualization")
    print("  ✓ APIs and async programming")
    print("  ✓ Testing and type hints")
    print("  ✓ Complete ETL pipelines")
    print("\nYou're now ready for:")
    print("  → Data Engineering projects")
    print("  → AI/ML applications")
    print("  → 100 Days of Data and AI bootcamp")
    print("\nKeep coding and building! 🚀")
    print("="*70)
