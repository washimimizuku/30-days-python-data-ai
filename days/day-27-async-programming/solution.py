"""
Day 27: Async Programming Basics - Solutions
"""

import asyncio
import time

print("="*60)
print("Day 27: Async Programming")
print("="*60)
print()

# Exercise 1
print("Exercise 1: Basic async/await")

async def hello_async():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    return "Done"

# Run async function
result = asyncio.run(hello_async())
print(f"Result: {result}")
print()

# Exercise 2
print("Exercise 2: Multiple Async Tasks")

async def task(name, delay):
    print(f"Task {name} starting...")
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay}s")
    return f"Result from {name}"

async def run_multiple_tasks():
    # Create tasks
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))
    task3 = asyncio.create_task(task("C", 3))
    
    # Wait for all
    results = await asyncio.gather(task1, task2, task3)
    return results

start = time.time()
results = asyncio.run(run_multiple_tasks())
elapsed = time.time() - start

print(f"Results: {results}")
print(f"Total time: {elapsed:.2f}s (concurrent execution)")
print()

# Exercise 3
print("Exercise 3: Async with Real Operations")

async def fetch_data(sensor_id, delay):
    """Simulate API call to fetch sensor data"""
    print(f"Fetching data from sensor {sensor_id}...")
    await asyncio.sleep(delay)  # Simulate network delay
    return {
        "sensor_id": sensor_id,
        "temperature": 20 + sensor_id,
        "timestamp": time.time()
    }

async def fetch_all_sensors():
    sensors = [101, 102, 103, 104, 105]
    tasks = [fetch_data(sid, 1) for sid in sensors]
    results = await asyncio.gather(*tasks)
    return results

start = time.time()
sensor_data = asyncio.run(fetch_all_sensors())
elapsed = time.time() - start

print(f"Fetched {len(sensor_data)} sensors in {elapsed:.2f}s")
for data in sensor_data:
    print(f"  Sensor {data['sensor_id']}: {data['temperature']}°C")
print()

# Exercise 4
print("Exercise 4: Gather Results with Error Handling")

async def fetch_with_error(sensor_id):
    await asyncio.sleep(0.5)
    if sensor_id == 103:
        raise Exception(f"Sensor {sensor_id} offline")
    return {"sensor_id": sensor_id, "value": sensor_id * 10}

async def fetch_all_with_handling():
    sensors = [101, 102, 103, 104]
    tasks = [fetch_with_error(sid) for sid in sensors]
    
    # gather with return_exceptions=True
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    successful = []
    failed = []
    
    for result in results:
        if isinstance(result, Exception):
            failed.append(str(result))
        else:
            successful.append(result)
    
    return successful, failed

successful, failed = asyncio.run(fetch_all_with_handling())
print(f"Successful: {len(successful)}")
print(f"Failed: {len(failed)}")
if failed:
    print(f"Errors: {failed}")
print()

# Exercise 5
print("Exercise 5: Async Data Processing Pipeline")

async def fetch_raw_data(source_id):
    """Simulate fetching data"""
    await asyncio.sleep(0.5)
    return [source_id * 10 + i for i in range(5)]

async def process_data(data):
    """Simulate processing"""
    await asyncio.sleep(0.3)
    return [x * 2 for x in data]

async def save_data(processed_data, source_id):
    """Simulate saving"""
    await asyncio.sleep(0.2)
    return f"Saved {len(processed_data)} items from source {source_id}"

async def pipeline(source_id):
    """Complete async pipeline"""
    raw = await fetch_raw_data(source_id)
    processed = await process_data(raw)
    result = await save_data(processed, source_id)
    return result

async def run_pipeline():
    sources = [1, 2, 3, 4]
    tasks = [pipeline(sid) for sid in sources]
    results = await asyncio.gather(*tasks)
    return results

start = time.time()
pipeline_results = asyncio.run(run_pipeline())
elapsed = time.time() - start

print("Pipeline results:")
for result in pipeline_results:
    print(f"  {result}")
print(f"Total time: {elapsed:.2f}s")
print()

# Bonus: Sync vs Async Comparison
print("Bonus: Sync vs Async Comparison")

def sync_task(n):
    time.sleep(1)
    return n * 2

async def async_task(n):
    await asyncio.sleep(1)
    return n * 2

# Synchronous
start = time.time()
sync_results = [sync_task(i) for i in range(5)]
sync_time = time.time() - start

# Asynchronous
async def run_async_tasks():
    tasks = [async_task(i) for i in range(5)]
    return await asyncio.gather(*tasks)

start = time.time()
async_results = asyncio.run(run_async_tasks())
async_time = time.time() - start

print(f"Synchronous: {sync_time:.2f}s")
print(f"Asynchronous: {async_time:.2f}s")
print(f"Speedup: {sync_time/async_time:.2f}x")

print("\n" + "="*60)
print("Day 27 Complete! Move to Day 28")
print("="*60)
