"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy import Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    relationship,
)
import config

from sqlalchemy import create_engine


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)
SQLALCHEMY_ECHO = True


engine = create_async_engine(
    url=PG_CONN_URI,
    echo=SQLALCHEMY_ECHO,
    pool_size=50,
    max_overflow=10,
)
Session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{(cls.__name__).lower()}s"

    metadata = MetaData(
        naming_convention=config.SQLALCHEMY_NAMING_CONVENTION,
    )


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String)
    username: Mapped[String] = mapped_column(String)
    email: Mapped[String] = mapped_column(String)

    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")


class Post(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[String] = mapped_column(String)
    body: Mapped[String] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")
