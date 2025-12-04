"""
Day 20: Mini Project - Data Analysis Tool - Solution
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
import os

class DataAnalyzer:
    def __init__(self):
        self.data = None
        self.clean_data_df = None
        self.results = {}
    
    def load_data(self, filename):
        """Load data from CSV"""
        filepath = f"data/raw/{filename}"
        print(f"Loading data from {filepath}...")
        self.data = pd.read_csv(filepath, parse_dates=["timestamp"])
        print(f"Loaded {len(self.data)} rows")
        return self
    
    def clean_data(self):
        """Clean and validate data"""
        print("Cleaning data...")
        df = self.data.copy()
        
        # Remove duplicates
        initial_count = len(df)
        df = df.drop_duplicates()
        duplicates_removed = initial_count - len(df)
        
        # Handle missing values
        missing_before = df.isnull().sum().sum()
        df = df.dropna(subset=["sensor_id", "temperature"])
        df["humidity"] = df["humidity"].fillna(df["humidity"].mean())
        
        # Remove outliers
        Q1 = df["temperature"].quantile(0.25)
        Q3 = df["temperature"].quantile(0.75)
        IQR = Q3 - Q1
        df = df[
            (df["temperature"] >= Q1 - 1.5 * IQR) &
            (df["temperature"] <= Q3 + 1.5 * IQR)
        ]
        
        self.clean_data_df = df
        self.results["cleaning"] = {
            "duplicates_removed": duplicates_removed,
            "missing_values_handled": int(missing_before),
            "outliers_removed": initial_count - len(df) - duplicates_removed,
            "final_row_count": len(df)
        }
        
        print(f"Cleaned: {len(df)} rows remaining")
        return self
    
    def analyze(self):
        """Perform statistical analysis"""
        print("Analyzing data...")
        df = self.clean_data_df
        
        # Overall statistics
        self.results["overall_stats"] = {
            "temperature": {
                "mean": float(df["temperature"].mean()),
                "median": float(df["temperature"].median()),
                "std": float(df["temperature"].std()),
                "min": float(df["temperature"].min()),
                "max": float(df["temperature"].max())
            },
            "humidity": {
                "mean": float(df["humidity"].mean()),
                "median": float(df["humidity"].median()),
                "std": float(df["humidity"].std()),
                "min": float(df["humidity"].min()),
                "max": float(df["humidity"].max())
            }
        }
        
        # Group by sensor
        sensor_stats = df.groupby("sensor_id").agg({
            "temperature": ["count", "mean", "std"],
            "humidity": ["mean", "std"]
        }).round(2)
        
        self.results["by_sensor"] = {}
        for sensor_id in df["sensor_id"].unique():
            sensor_data = df[df["sensor_id"] == sensor_id]
            self.results["by_sensor"][int(sensor_id)] = {
                "count": len(sensor_data),
                "temperature_mean": float(sensor_data["temperature"].mean()),
                "humidity_mean": float(sensor_data["humidity"].mean())
            }
        
        # Time-based analysis
        df["hour"] = df["timestamp"].dt.hour
        hourly_avg = df.groupby("hour")[["temperature", "humidity"]].mean()
        
        self.results["hourly_patterns"] = {
            "peak_temp_hour": int(hourly_avg["temperature"].idxmax()),
            "peak_temp_value": float(hourly_avg["temperature"].max()),
            "lowest_temp_hour": int(hourly_avg["temperature"].idxmin()),
            "lowest_temp_value": float(hourly_avg["temperature"].min())
        }
        
        print("Analysis complete")
        return self
    
    def export_results(self, filename):
        """Export results to JSON"""
        print(f"Exporting results to {filename}...")
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "analysis_results": self.results,
            "summary": {
                "total_sensors": len(self.clean_data_df["sensor_id"].unique()),
                "total_readings": len(self.clean_data_df),
                "avg_temperature": round(self.clean_data_df["temperature"].mean(), 2),
                "avg_humidity": round(self.clean_data_df["humidity"].mean(), 2)
            }
        }
        
        os.makedirs("data/processed", exist_ok=True)
        filepath = f"data/processed/{filename}"
        with open(filepath, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"Results exported successfully")
        return self
    
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "="*50)
        print("DATA ANALYSIS SUMMARY")
        print("="*50)
        
        if "cleaning" in self.results:
            print("\nData Cleaning:")
            for key, value in self.results["cleaning"].items():
                print(f"  {key.replace('_', ' ').title()}: {value}")
        
        if "overall_stats" in self.results:
            print("\nOverall Statistics:")
            print(f"  Temperature: {self.results['overall_stats']['temperature']['mean']:.2f}°C (±{self.results['overall_stats']['temperature']['std']:.2f})")
            print(f"  Humidity: {self.results['overall_stats']['humidity']['mean']:.2f}% (±{self.results['overall_stats']['humidity']['std']:.2f})")
        
        if "by_sensor" in self.results:
            print("\nBy Sensor:")
            for sensor_id, stats in self.results["by_sensor"].items():
                print(f"  Sensor {sensor_id}: {stats['count']} readings, {stats['temperature_mean']:.2f}°C avg")
        
        print("="*50)

# Main execution
if __name__ == "__main__":
    # Create sample dataset
    print("Creating sample dataset...")
    np.random.seed(42)
    
    dates = pd.date_range("2024-01-01", periods=100, freq="H")
    data = {
        "timestamp": dates,
        "sensor_id": np.random.choice([101, 102, 103, 104], 100),
        "temperature": np.concatenate([
            np.random.normal(25, 2, 95),
            [np.nan, 60, -10, np.nan, 55]  # Some bad data
        ]),
        "humidity": np.random.uniform(40, 80, 100)
    }
    
    df = pd.DataFrame(data)
    # Add some duplicates
    df = pd.concat([df, df.iloc[:5]], ignore_index=True)
    
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/sensor_data_raw.csv", index=False)
    print(f"Created data/raw/sensor_data_raw.csv with {len(df)} rows\n")
    
    # Run analysis pipeline
    analyzer = DataAnalyzer()
    analyzer.load_data("sensor_data_raw.csv")
    analyzer.clean_data()
    analyzer.analyze()
    analyzer.export_results("analysis_results.json")
    analyzer.print_summary()
    
    print("\n✅ Project Complete!")
    
    # Cleanup
    for folder in ["data/raw", "data/processed"]:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f != ".gitkeep":
                    filepath = os.path.join(folder, f)
                    if os.path.isfile(filepath):
                        os.remove(filepath)
