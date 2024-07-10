# example of waiting for the first task to complete
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 to 1
    value = random()
    await asyncio.sleep(value)
    print(f'>task {arg} done with {value}')
    if value < 0.5:
        raise Exception(f'Something bad happened in {arg}')
    
async def main():
   
    tasks = [asyncio.create_task(task_coro(i))for i in range(10)]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

    first = done.pop()
    print(first)


asyncio.run(main())
