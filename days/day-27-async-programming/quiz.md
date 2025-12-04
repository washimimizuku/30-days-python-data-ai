# Day 27 Quiz: Async Programming

## Questions

### 1. What does async/await do?

**Your answer:**


**Correct answer:** `async` defines a coroutine function that can be paused and resumed. `await` pauses execution until the awaited operation completes, allowing other tasks to run meanwhile.

---

### 2. When should you use async programming?

**Your answer:**


**Correct answer:** Use async for I/O-bound operations (network requests, file I/O, database queries) where you're waiting for external resources. Not beneficial for CPU-bound tasks.

---

### 3. What does asyncio.gather() do?

**Your answer:**


**Correct answer:** Runs multiple coroutines concurrently and collects their results in order. Use `return_exceptions=True` to handle errors without stopping other tasks.

---

### 4. How do you run an async function?

**Your answer:**


**Correct answer:** Use `asyncio.run(async_function())` for the main entry point. Inside async functions, use `await async_function()` or `asyncio.create_task()`.

---

### 5. What's the difference between concurrent and parallel?

**Your answer:**


**Correct answer:** Concurrent means tasks make progress by switching between them (async). Parallel means tasks run simultaneously on multiple CPU cores (multiprocessing). Async is concurrent, not parallel.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 28: Type Hints and Pydantic
