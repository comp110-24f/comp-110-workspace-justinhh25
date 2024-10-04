"""Lets us get and print coordinates"""

__author__ = "730758900"


def get_coords(xs: str, ys: str) -> None:
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
