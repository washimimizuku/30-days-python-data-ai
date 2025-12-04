# Day 27: Async Programming Basics

## 📖 Learning Objectives
- Understand async/await syntax
- Run concurrent operations
- Use asyncio.gather()
- Handle async errors
- Know when to use async

## Theory

### Why Async?
For I/O-bound operations (network, files):
- Run multiple operations concurrently
- Don't wait idle for responses
- Much faster for many requests

### Basic Async
```python
import asyncio

async def fetch_data(id):
    await asyncio.sleep(1)  # Simulate I/O
    return f"Data {id}"

# Run async function
result = asyncio.run(fetch_data(1))
```

### Concurrent Execution
```python
async def main():
    # Run concurrently
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    return results

results = asyncio.run(main())
```

### When to Use Async
✅ Use for: Network requests, file I/O, database queries
❌ Don't use for: CPU-intensive calculations

## 💻 Exercises
Complete `exercise.py`

## Tomorrow: Day 28 - Type Hints
