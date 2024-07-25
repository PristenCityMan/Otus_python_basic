from abc import ABC
from Otus_python_basic.homework_02.exceptions import *


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_fuel(self, fuel):
        self.fuel = fuel

    def set_started(self, started):
        self.started = started

    def start(self):
        if self.started:
            if self.fuel > 0:
                self.set_started(self, True)
            else:
                raise LowFuelError

    def move(self, distance):
        if distance * self.fuel_consumption > self.fuel:
            raise NotEnoughFuel
        else:
            self.set_fuel(self, self.fuel - distance * self.fuel_consumption)
