"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    print("Топливо отсутствует!")


class NotEnoughFuel(Exception):
    print("Недостаточно топлива для преодоления дистанции!")


class CargoOverload(Exception):
    print("Транспорт перегружен")
