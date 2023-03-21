import asyncio
import aiohttp
import requests
from datetime import datetime


async def asynchronous_task():
    start_time = datetime.now()
    print("We are going to perform an asynchronous operation")
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                print(i ,"->",await resp.json())
    end_time = datetime.now()
    print('Duration async: {}'.format(end_time - start_time))


def synchronous_task():
    start_time = datetime.now()
    print("We are going to perform an synchronous operation")
    for i in range(10):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        print(i ,"->",response.json())
    end_time = datetime.now()
    print('Duration sync: {}'.format(end_time - start_time))


def main():
    asyncio.run(asynchronous_task())
    synchronous_task() 


main()