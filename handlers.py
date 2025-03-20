import asyncio 


async def startup():
    print("statring...")
    await asyncio.sleep(5)
    print("started")
