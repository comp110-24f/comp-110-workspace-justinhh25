"""Mutating functions."""

__author__ = "730758900"


def manual_append(intList: list[int], digit: int) -> None:  # appends a digit to the list of ints
    intList.append(digit)


def double(intList2: list[int]) -> None:  # iterates through the list and doubles each element
    i: int = 0
    while i < len(intList2):
        intList2[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]  # global variables: list 2 is set to list 1 so they are in same heap
list_2: list[int] = list_1

double(list_2)  # both lists will be doubled since they point to same heap
print(list_1)
print(list_2)
