from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from .flask_db import db
from .int_id_pk_mixin import IntIdPkMixin


class Post(IntIdPkMixin, db.Model):
    title: Mapped[String] = mapped_column(String)
    body: Mapped[String] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")


def __str__(self):
    return (
        f"{self.__class__.__name__}("
        f"id={self.id}, "
        f"name={self.title!r}, "
        f"name={self.boby!r}, "
        f")"
    )

    def __repr__(self):
        return str(self)
