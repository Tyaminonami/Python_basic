"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, *engine):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def __str__(self):
        return f"weight = {self.weight}, fuel = {self.fuel}, " \
               f"fuel_consumption = {self.fuel_consumption}, status = {self.started}, " \
               f"car has engine with {self.engine}"

    def set_engine(self, engine):
        self.engine = engine




