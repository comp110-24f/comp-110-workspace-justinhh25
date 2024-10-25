"""Toolboxes of functions to use on lists"""

__author__: str = "730758900"


def all(intList: list[int], intElem: int) -> bool:
    """Checks if all elements in the list are equal to the selected element"""
    if len(intList) == 0:  # edge case: if list is empty returns False
        return False

    idx: int = 0

    while idx < len(intList):  # returns false if any index in the list != to intElem
        if intList[idx] != intElem:
            return False
        idx += 1
    return True  # if it doesn't return False, then it will return True


def max(input: list[int]) -> int:
    """Looks for the maximum value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # checks if list is empty

    maxValue: int = input[0]  # maxValue is first elem in list
    idx: int = 1  # since first elem is accounted for, we start at the next index

    while idx < len(input):
        currentValue: int = input[
            idx
        ]  # current value that the loop is iterating through
        if currentValue > maxValue:
            maxValue = (
                currentValue  # maxValue gets currentValue if it's greater than it
            )
        idx += 1
    return maxValue


def is_equal(int1: list[int], int2: list[int]) -> bool:
    """Checks if two lists are equal to each other"""
    if len(int1) != len(int2):  # checks to see if lists don't have same length
        return False
    for idx in range(0, len(int1)):  # checks each individual element in list
        if int1[idx] != int2[idx]:  # if an element isn't the same, returns False
            return False
    return True  # if all elements are equal, returns True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends one list to another list"""
    for x in list2:  # for loop to iterate through list2 and append each element to
        #  list1
        list1.append(x)
