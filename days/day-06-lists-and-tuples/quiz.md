# Day 6 Quiz: Lists and Tuples

## Questions

### 1. What is the difference between a list and a tuple?

**Your answer:**


**Correct answer:** Lists are mutable (can be changed after creation) and use square brackets `[]`. Tuples are immutable (cannot be changed) and use parentheses `()`. Lists have methods like append() and remove(), while tuples don't.

---

### 2. What does `numbers[-1]` return?

**Your answer:**


**Correct answer:** The last element of the list. Negative indices count from the end: -1 is last, -2 is second-to-last, etc.

---

### 3. What's the result of `[1, 2, 3, 4, 5][1:4]`?

**Your answer:**


**Correct answer:** `[2, 3, 4]` - Slicing includes the start index (1) but excludes the end index (4).

---

### 4. How do you add an element to the end of a list?

**Your answer:**


**Correct answer:** Use the `append()` method: `my_list.append(element)`. Alternatively, use `my_list += [element]` or `my_list.extend([element])`.

---

### 5. Can you modify a tuple after creation?

**Your answer:**


**Correct answer:** No, tuples are immutable. Once created, you cannot change, add, or remove elements. You must create a new tuple instead.

---

## Score Yourself

- 5/5: Excellent! You understand lists and tuples
- 3-4/5: Good! Review the concepts you missed
- 0-2/5: Review today's lesson and try exercises again

## Next Steps

- If you scored 4-5: Move to Day 7
- If you scored 0-3: Review `README.md` and try exercises again
