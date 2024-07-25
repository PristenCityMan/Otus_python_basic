"""
создайте класс `Plane`, наследник `Vehicle`
"""

from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    max_cargo = 0
    cargo = 0

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, load_cargo):
        if self.cargo + load_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += self.cargo + load_cargo

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
