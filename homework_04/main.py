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
from jsonplaceholder_requests import fetch_posts, fetch_users
from sqlalchemy.ext.asyncio import AsyncSession


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_main():
    async with Session() as session:
        ct = await create_tables()


async def create_owner(
    session: AsyncSession,
    name: str,
    username: str,
) -> Owner:
    owner = Owner(
        name=name,
        username=username,
    )
    session.add(owner)
    await session.commit()
    # await session.refresh(owner)
    return owner


def main():
    pass


if __name__ == "__main__":
    main()
