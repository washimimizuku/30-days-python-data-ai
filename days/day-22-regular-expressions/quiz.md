# Day 22 Quiz: Regular Expressions

## Questions

### 1. What does the `\d` pattern match?

**Your answer:**


**Correct answer:** `\d` matches any digit (0-9). It's equivalent to `[0-9]`. Use `\d+` to match one or more digits, `\d{3}` to match exactly 3 digits.

---

### 2. What's the difference between `search()` and `match()`?

**Your answer:**


**Correct answer:** `search()` finds a pattern anywhere in the string, while `match()` only checks if the pattern matches at the beginning of the string. Use `search()` for general pattern finding.

---

### 3. How do you extract data using groups?

**Your answer:**


**Correct answer:** Use parentheses `()` to create groups, then access with `.group(1)`, `.group(2)`, etc. Named groups use `(?P<name>pattern)` and access with `.group('name')`.

---

### 4. What does the `+` quantifier mean?

**Your answer:**


**Correct answer:** `+` means "one or more" of the preceding pattern. Example: `\d+` matches one or more digits. Other quantifiers: `*` (zero or more), `?` (zero or one), `{n}` (exactly n).

---

### 5. How do you match a literal dot (.) in regex?

**Your answer:**


**Correct answer:** Escape it with backslash: `\.` because `.` is a special character that matches any character. Always escape special characters: `. ^ $ * + ? { } [ ] \ | ( )`.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 23: Virtual Environments and pip
