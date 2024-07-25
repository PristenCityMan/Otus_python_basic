"""
создайте класс `Car`, наследник `Vehicle`
"""

from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    engine: Engine

    def set_engine(self, new_engine: "Engine") -> "Engine":
        self.engine = new_engine
