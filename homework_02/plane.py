"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    max_cargo = 0
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
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
