"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload as e3


class Plane(Vehicle):

    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, a):
        if self.max_cargo < a + self.cargo:
            raise e3
        else:
            self.cargo += a

    def remove_all_cargo(self):
        a = self.cargo
        self.cargo = 0
        return a

    def __str__(self):
        return f"weight = {self.weight}, fuel = {self.fuel}, " \
               f"fuel_consumption = {self.fuel_consumption}, status = {self.started}, cargo" \
               f" = {self.cargo}, max. cargo = {self.max_cargo}"
