"""Summing the elements of a list using different loops"""

__author__: str = "730758900"


def w_sum(vals: list[float]) -> float:
    """Uses a while loop to add elements in list"""
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Uses a for in loop to iterate through numbers in list"""
    sum: float = 0.0
    for number in vals:
        sum += number
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Uses the index in a for in loop to sum numbers in a list"""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum


print(f_range_sum([1.1, 0.9, 1.0]))
