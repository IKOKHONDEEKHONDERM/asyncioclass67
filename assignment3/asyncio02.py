# example of running a coroutine


import asyncio
async def custom_coro():
    await asyncio.sleep(1)

async def main():
   #execute my custom 
   await custom_coro()

#start the coroutine program
asyncio.run(main())