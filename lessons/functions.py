"""Practice with functions."""

from random import randint

print(randint(3, 17))


def sum(num1: int, num2: int) -> int:
    return num1 + num2


print(sum(num1=13, num2=2))
