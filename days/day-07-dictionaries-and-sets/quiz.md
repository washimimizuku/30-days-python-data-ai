# Day 7 Quiz: Dictionaries and Sets

## Questions

### 1. What is the main difference between a dictionary and a list?

**Your answer:**


**Correct answer:** Dictionaries store key-value pairs and access elements by key, while lists store ordered elements accessed by index. Dictionaries are unordered (before Python 3.7) or insertion-ordered (3.7+), while lists maintain order by position.

---

### 2. What happens if you try to access a dictionary key that doesn't exist?

**Your answer:**


**Correct answer:** Python raises a `KeyError`. To avoid this, use the `get()` method with a default value: `dict.get(key, default_value)`.

---

### 3. What makes sets different from lists?

**Your answer:**


**Correct answer:** Sets only store unique values (no duplicates), are unordered, and don't support indexing. Sets are optimized for membership testing and set operations (union, intersection, difference).

---

### 4. How do you add a new key-value pair to a dictionary?

**Your answer:**


**Correct answer:** Use assignment: `my_dict[new_key] = new_value`. This creates the key if it doesn't exist, or updates it if it does.

---

### 5. What's the result of `{1, 2, 3} & {2, 3, 4}`?

**Your answer:**


**Correct answer:** `{2, 3}` - The `&` operator performs set intersection, returning only elements present in both sets.

---

## Score Yourself

- 5/5: Excellent! You understand dictionaries and sets
- 3-4/5: Good! Review the concepts you missed
- 0-2/5: Review today's lesson and try exercises again

## Next Steps

- If you scored 4-5: Move to Day 8
- If you scored 0-3: Review `README.md` and try exercises again
