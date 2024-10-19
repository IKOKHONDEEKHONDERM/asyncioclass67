
from random import random  
import asyncio  


async def producer(queue):
    print('Producer: Running')

    for i in range(10):
        value = i
        await asyncio.sleep(random())
       
        print(f"Producer put {value} into the queue")
        await queue.put(value)

    await queue.put(None)
    print('Producer: Done')

async def consumer(queue):
    print('Consumer: Running')
    
    while True:
        
        item = await queue.get()
       
        if item is None:
            break
       
        print(f"Consumer got {item}")
   
    print('Consumer: Done')


async def main():
   
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))
asyncio.run(main())