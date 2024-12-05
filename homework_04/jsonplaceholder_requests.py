"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from dataclasses import dataclass
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
KEYS_USERS = ("id", "name", "username", "email")
KEYS_POSTS = ("id", "userId", "title", "body")


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def filter_data(KEYS: tuple, URL: str) -> dict:
    try:
        data: dict = await fetch_json(URL)
    except aiohttp.ClientError as ex:
        print("can't fetch users")
        return None
    data_filtred: list = []
    for element in data:
        user_filtred: dict = {
            key: field for key, field in element.items() if key in KEYS
        }
        data_filtred.append(user_filtred)
    print(data_filtred)
    return data_filtred


async def main():
    await asyncio.gather(
        filter_data(KEYS_USERS, USERS_DATA_URL),
        filter_data(KEYS_POSTS, POSTS_DATA_URL),
    )


if __name__ == "__main__":
    asyncio.run(main())
