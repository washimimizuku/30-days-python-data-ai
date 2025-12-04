# Day 25: Matplotlib - Data Visualization

## 📖 Learning Objectives
- Create line plots, scatter plots, bar charts
- Customize plots (colors, labels, legends)
- Create subplots
- Save figures
- Build dashboards

## Theory

### Basic Plotting
```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()

# Scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.colorbar()
plt.show()

# Bar chart
plt.bar(categories, values)
plt.show()
```

### Customization
```python
plt.plot(x, y, 
         color='blue',
         linestyle='--',
         linewidth=2,
         marker='o',
         label='Data')
plt.legend()
plt.grid(True, alpha=0.3)
```

### Subplots
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data, bins=30)

plt.tight_layout()
plt.show()
```

### Saving Figures
```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf')  # Vector format
```

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 26 - APIs and Requests
