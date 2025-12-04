"""
Day 25: Matplotlib - Data Visualization - Solutions
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("="*60)
print("Day 25: Matplotlib Visualization")
print("="*60)
print()

# Exercise 1
print("Exercise 1: Basic Plots")

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 4))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.savefig('line_plot.png')
plt.close()
print("✓ Created line plot")

# Scatter plot
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('scatter_plot.png')
plt.close()
print("✓ Created scatter plot")

# Bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue', edgecolor='navy')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.savefig('bar_chart.png')
plt.close()
print("✓ Created bar chart")
print()

# Exercise 2
print("Exercise 2: Customization")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)
plt.title('Trigonometric Functions', fontsize=16, fontweight='bold')
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig('customized_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Created customized plot")
print()

# Exercise 3
print("Exercise 3: Multiple Subplots")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Line plot
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True)

# Subplot 2: Scatter
x = np.random.rand(50)
y = np.random.rand(50)
axes[0, 1].scatter(x, y, alpha=0.5)
axes[0, 1].set_title('Random Scatter')

# Subplot 3: Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
axes[1, 0].bar(categories, values)
axes[1, 0].set_title('Bar Chart')

# Subplot 4: Histogram
data = np.random.normal(0, 1, 1000)
axes[1, 1].hist(data, bins=30, edgecolor='black')
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.savefig('subplots.png')
plt.close()
print("✓ Created subplot grid")
print()

# Exercise 4
print("Exercise 4: Sensor Data Visualization")

# Create sample sensor data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='H')
temp_data = pd.DataFrame({
    'timestamp': dates,
    'sensor_A': 20 + 5 * np.sin(np.linspace(0, 4*np.pi, 100)) + np.random.normal(0, 1, 100),
    'sensor_B': 22 + 3 * np.cos(np.linspace(0, 4*np.pi, 100)) + np.random.normal(0, 1, 100),
    'sensor_C': 25 + 4 * np.sin(np.linspace(0, 3*np.pi, 100)) + np.random.normal(0, 1, 100)
})

# Time series plot
plt.figure(figsize=(12, 6))
plt.plot(temp_data['timestamp'], temp_data['sensor_A'], label='Sensor A', alpha=0.7)
plt.plot(temp_data['timestamp'], temp_data['sensor_B'], label='Sensor B', alpha=0.7)
plt.plot(temp_data['timestamp'], temp_data['sensor_C'], label='Sensor C', alpha=0.7)
plt.title('Temperature Readings Over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('time_series.png')
plt.close()
print("✓ Created time series plot")

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(temp_data['sensor_A'], bins=20, alpha=0.5, label='Sensor A', edgecolor='black')
plt.hist(temp_data['sensor_B'], bins=20, alpha=0.5, label='Sensor B', edgecolor='black')
plt.hist(temp_data['sensor_C'], bins=20, alpha=0.5, label='Sensor C', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('histogram.png')
plt.close()
print("✓ Created histogram")

# Box plot
plt.figure(figsize=(8, 6))
data_for_box = [temp_data['sensor_A'], temp_data['sensor_B'], temp_data['sensor_C']]
plt.boxplot(data_for_box, labels=['Sensor A', 'Sensor B', 'Sensor C'])
plt.title('Temperature Distribution by Sensor')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.savefig('boxplot.png')
plt.close()
print("✓ Created box plot")
print()

# Exercise 5
print("Exercise 5: Complete Dashboard")

fig = plt.figure(figsize=(15, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Main time series (top, spanning 3 columns)
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(temp_data['timestamp'], temp_data['sensor_A'], label='Sensor A')
ax1.plot(temp_data['timestamp'], temp_data['sensor_B'], label='Sensor B')
ax1.plot(temp_data['timestamp'], temp_data['sensor_C'], label='Sensor C')
ax1.set_title('Sensor Dashboard - Temperature Monitoring', fontsize=16, fontweight='bold')
ax1.set_ylabel('Temperature (°C)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Statistics (middle row)
ax2 = fig.add_subplot(gs[1, 0])
means = [temp_data['sensor_A'].mean(), temp_data['sensor_B'].mean(), temp_data['sensor_C'].mean()]
ax2.bar(['A', 'B', 'C'], means, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax2.set_title('Average Temperature')
ax2.set_ylabel('°C')

ax3 = fig.add_subplot(gs[1, 1])
ax3.boxplot(data_for_box, labels=['A', 'B', 'C'])
ax3.set_title('Distribution')
ax3.set_ylabel('°C')

ax4 = fig.add_subplot(gs[1, 2])
stds = [temp_data['sensor_A'].std(), temp_data['sensor_B'].std(), temp_data['sensor_C'].std()]
ax4.bar(['A', 'B', 'C'], stds, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax4.set_title('Std Deviation')
ax4.set_ylabel('°C')

# Detailed views (bottom row)
ax5 = fig.add_subplot(gs[2, 0])
ax5.hist(temp_data['sensor_A'], bins=15, color='#FF6B6B', alpha=0.7, edgecolor='black')
ax5.set_title('Sensor A Distribution')
ax5.set_xlabel('°C')

ax6 = fig.add_subplot(gs[2, 1])
ax6.hist(temp_data['sensor_B'], bins=15, color='#4ECDC4', alpha=0.7, edgecolor='black')
ax6.set_title('Sensor B Distribution')
ax6.set_xlabel('°C')

ax7 = fig.add_subplot(gs[2, 2])
ax7.hist(temp_data['sensor_C'], bins=15, color='#45B7D1', alpha=0.7, edgecolor='black')
ax7.set_title('Sensor C Distribution')
ax7.set_xlabel('°C')

plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Created complete dashboard")

# Cleanup
import os
for f in ['line_plot.png', 'scatter_plot.png', 'bar_chart.png', 'customized_plot.png',
          'subplots.png', 'time_series.png', 'histogram.png', 'boxplot.png', 'dashboard.png']:
    if os.path.exists(f):
        os.remove(f)

print("\n" + "="*60)
print("Day 25 Complete! Move to Day 26")
print("="*60)
