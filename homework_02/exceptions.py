"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass

class CargoOverload(Exception):
    pass

class NotEnoughFuel(Exception):
    pass
