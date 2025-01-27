from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .flask_db import db
from .int_id_pk_mixin import IntIdPkMixin


class User(IntIdPkMixin, db.Model):
    name: Mapped[String] = mapped_column(String)
    username: Mapped[String] = mapped_column(String)
    email: Mapped[String] = mapped_column(String)

    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")


def __str__(self):
    return (
        f"{self.__class__.__name__}("
        f"id={self.id}, "
        f"name={self.name!r}, "
        f"name={self.username!r}, "
        f"name={self.email!r}, "
        f")"
    )

    def __repr__(self):
        return str(self)
