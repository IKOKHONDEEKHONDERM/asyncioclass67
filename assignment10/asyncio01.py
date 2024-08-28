# Example of using an asyncio queue
from random import random  
import asyncio  

# Coroutine to generate work (Producer)
async def producer(queue):
    print('Producer: Running')
    # Generate work
    for i in range(10):
        # Generate a value
        value = i
        # Block to simulate work
        await asyncio.sleep(random())
        # Add the value to the queue
        print(f"Producer put {value} into the queue")
        await queue.put(value)
    # Send a signal to indicate all work is done
    await queue.put(None)
    print('Producer: Done')

# Coroutine to consume work (Consumer)
async def consumer(queue):
    print('Consumer: Running')
    # Consume work
    while True:
        # Get a unit of work from the queue
        item = await queue.get()
        # Check for stop signal
        if item is None:
            break
        # Report the consumed item
        print(f"Consumer got {item}")
    # Indicate that all work is done
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumer concurrently
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())