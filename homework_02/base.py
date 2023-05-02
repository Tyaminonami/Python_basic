from abc import ABC

from homework_02.exceptions import NotEnoughFuel as e1
from homework_02.exceptions import LowFuelError as e2


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"weight = {self.weight}, fuel = {self.fuel}, " \
               f"fuel_consumption = {self.fuel_consumption}, status = {self.started}"

    def start(self):
        if self.started == False:
            if self.fuel <= 0:
                raise e2
            else:
                self.started = True
        pass

    def move(self, a):
        b = self.fuel / self.fuel_consumption
        if a <= b:
            self.fuel -= a * self.fuel_consumption
            return self.fuel
        else:
            raise e1

