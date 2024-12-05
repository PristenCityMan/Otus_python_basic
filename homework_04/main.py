"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

from models import engine, Base, Session
import asyncio
from jsonplaceholder_requests import (
    filter_data,
    USERS_DATA_URL,
    POSTS_DATA_URL,
    KEYS_USERS,
    KEYS_POSTS,
)
from models import User, Post
from sqlalchemy.ext.asyncio import AsyncSession


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(
    session: AsyncSession, id: int, name: str, username: str, email: str
) -> User:
    user = User(id=id, name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    return user


async def create_post(
    session: AsyncSession, id: int, title: str, body: str, user_id: int
) -> Post:
    post = Post(id=id, title=title, body=body, user_id=user_id)
    session.add(post)
    await session.commit()
    return post


async def async_main():
    async with AsyncSession() as session:
        await create_tables()
        users_data: list[dict]
        posts_data: list[dict]
        users_data, posts_data = await asyncio.gather(
            filter_data(KEYS_USERS, USERS_DATA_URL),
            filter_data(KEYS_POSTS, POSTS_DATA_URL),
        )


def main():
    pass


if __name__ == "__main__":
    asyncio.run(async_main())
