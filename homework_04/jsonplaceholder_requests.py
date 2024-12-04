"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from dataclasses import dataclass
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users() -> dict:
    try:
        data: dict = await fetch_json(USERS_DATA_URL)
    except aiohttp.ClientError as ex:
        print("can't fetch users")
        return None
    return {
        key: field
        for key, field in data.items()
        if key in ("id", "name", "username", "email")
    }


async def fetch_posts() -> dict:
    try:
        data: dict = await fetch_json(POSTS_DATA_URL)
    except aiohttp.ClientError as ex:
        print("can't fetch posts")
        return None
    return {
        key: field
        for key, field in data.items()
        if key in ("id", "userId", "title", "body")
    }
