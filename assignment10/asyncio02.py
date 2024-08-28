import asyncio
from random import random
import time  # Import time module to measure the total time taken

# Coroutine to generate work (Producer)
async def producer(queue):
    print('Producer: Running')
    start_time = time.time()  # Record the start time for producer
    # Generate work
    for i in range(10):
        # Generate a value
        value = i
        # Block to simulate work
        sleeptime = random()
        print(f"Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # Add the value to the queue
        print(f"Producer put {value}")
        await queue.put(value)
    # Send an all-done signal
    await queue.put(None)
    end_time = time.time()  # Record the end time for producer
    print('Producer: Done')
    producer_time = end_time - start_time
    print(f'Producer time taken: {producer_time:.2f} seconds')
    return producer_time

# Coroutine to consume work (Consumer)
async def consumer(queue):
    print('Consumer: Running')
    start_time = time.time()  # Record the start time for consumer
    # Consume work
    while True:
        # Get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # Check for stop
        if item is None:
            break
        # Report
        print(f"Consumer got {item}")
    end_time = time.time()  # Record the end time for consumer
    print('Consumer: Done')
    consumer_time = end_time - start_time
    print(f'Consumer time taken: {consumer_time:.2f} seconds')
    return consumer_time

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers concurrently, and gather their time results
    producer_time, consumer_time = await asyncio.gather(producer(queue), consumer(queue))
    # Calculate the total time taken by both producer and consumer
    total_time = producer_time + consumer_time
    print(f'Total time taken by producer and consumer: {total_time:.2f} seconds')

# Start the asyncio program
asyncio.run(main())
