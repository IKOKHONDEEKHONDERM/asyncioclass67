from random import random
import asyncio

async def task_rice():
    value_rice = random() + 1
    print('rice',value_rice)
    await asyncio.sleep(value_rice)
    return f'> task_rice done with {value_rice} seconds'

async def task_noodle():
    value_noodle = random() + 1
    print('noodle',value_noodle)
    await asyncio.sleep(value_noodle)
    return f'> task_noodle done with {value_noodle} seconds'

async def task_curry():
    value_curry = random() + 1
    print('curry',value_curry)
    await asyncio.sleep(value_curry)
    return f'> task_curry done with {value_curry} seconds'

async def main():
    tasks = []

    tasks.append(asyncio.create_task(task_rice(),name='rice'))
    tasks.append(asyncio.create_task(task_noodle(),name='noodle'))
    tasks.append(asyncio.create_task(task_curry(),name='curry'))
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first = done.pop()

    print(first.get_name(),(first.result()))


asyncio.run(main())
