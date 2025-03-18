import aiohttp
import asyncio
import user
import user.users


async def run():
    print(user)
    print(user.users.users)
    print("1133ddd")
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(run())