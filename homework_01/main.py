
"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
   return [i ** 2 for i in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(a):
    if a  <= 1:
        return False
    d = 2
    while d * d <= a and a % d != 0:
        d += 1
    return d * d > a



def filter_numbers(a, b):
    if b == ODD:
        return list(filter(lambda x: x % 2, a))
    elif b == EVEN:
        return list(filter(lambda x: x % 2 == 0, a))
    elif b == PRIME:
        return list(filter(is_prime, a))
