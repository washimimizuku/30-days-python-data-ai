# Day 21 Quiz: DateTime Handling

## Questions

### 1. What's the difference between datetime and date objects?

**Your answer:**


**Correct answer:** `datetime` includes both date and time (year, month, day, hour, minute, second), while `date` only includes year, month, and day. Use `datetime` when you need time precision, `date` for date-only operations.

---

### 2. How do you add 7 days to a datetime?

**Your answer:**


**Correct answer:** Use `timedelta`: `new_date = old_date + timedelta(days=7)`. You can also use `weeks`, `hours`, `minutes`, `seconds`, etc.

---

### 3. What does strftime() do?

**Your answer:**


**Correct answer:** `strftime()` formats a datetime object as a string using format codes. Example: `dt.strftime("%Y-%m-%d")` returns "2024-01-15". It's "string format time".

---

### 4. How do you parse a string into a datetime?

**Your answer:**


**Correct answer:** Use `strptime()`: `dt = datetime.strptime("2024-01-15", "%Y-%m-%d")`. The format string must match the input string exactly. It's "string parse time".

---

### 5. What is a Unix timestamp?

**Your answer:**


**Correct answer:** A Unix timestamp is the number of seconds since January 1, 1970 00:00:00 UTC (the "epoch"). Use `datetime.timestamp()` to convert to timestamp, `datetime.fromtimestamp()` to convert back.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 22: Regular Expressions
