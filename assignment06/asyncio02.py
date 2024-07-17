import asyncio
from re import A

class AsyncIterator():
    def __init__(self) :
        self.count = 0

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.count >= 10:
            raise StopAsyncIteration
        
        self.count += 1
        await asyncio.sleep(1)
        return self.count
    
async def main():
    async for item in AsyncIterator():
        print(item)

asyncio.run(main())