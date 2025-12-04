# Day 25 Quiz: Matplotlib Visualization

## Questions

### 1. What's the difference between plt.plot() and plt.scatter()?

**Your answer:**


**Correct answer:** `plt.plot()` creates line plots connecting points, while `plt.scatter()` creates scatter plots with individual points. Use plot for continuous data/trends, scatter for relationships between variables.

---

### 2. How do you create subplots?

**Your answer:**


**Correct answer:** Use `plt.subplots(rows, cols)` which returns figure and axes: `fig, axes = plt.subplots(2, 2)`. Access individual plots with `axes[row, col]`.

---

### 3. What does plt.savefig() do?

**Your answer:**


**Correct answer:** Saves the current figure to a file. Supports formats like PNG, PDF, SVG. Use `plt.savefig('plot.png', dpi=150, bbox_inches='tight')` for high quality.

---

### 4. How do you add a legend to a plot?

**Your answer:**


**Correct answer:** Add `label` parameter to plot functions, then call `plt.legend()`: `plt.plot(x, y, label='My Data')` followed by `plt.legend()`.

---

### 5. What's the purpose of plt.tight_layout()?

**Your answer:**


**Correct answer:** Automatically adjusts subplot spacing to prevent overlapping labels and titles. Always use before saving multi-subplot figures.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 26: Working with APIs
