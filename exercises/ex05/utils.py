"""Utils functions will go here"""

__author__: str = "730758900"


def only_evens(intList: list[int]) -> list[int]:
    """Finds only even numbers in a list and appends it to a new list"""
    evensList: list[int] = []  # creates new list for even numbers only
    for num in intList:  # loop to iterate list
        if num % 2 == 0:  # if there numbers have no remainder when divided by two
            evensList.append(num)  # it means they are even and appended to even list
    return evensList


def sub(intList: list[int], startIdx: int, endIdx: int) -> list[int]:
    """Takes a part of a list and creates its own sub list"""
    finalList: list[int] = []  # new list for elems to be appended to
    if startIdx < 0:  # if start index is less than zero, start at 0
        startIdx = 0
    if endIdx > len(intList):  # if endidx is greater than list length, stop at list end
        endIdx = len(intList)
    if len(intList) == 0 or startIdx >= len(intList) or endIdx <= 0:
        return finalList  # base case, returns empty list if above condition is met

    while startIdx < endIdx:
        finalList.append(intList[startIdx])  # appends starting index all the way
        startIdx += 1  # until it reaches the ending idx

    return finalList


def add_at_index(intList: list[int], addedInt: int, addedIdx: int) -> None:
    """Adds an elem at a specified idx position"""
    if addedIdx < 0 or addedIdx > len(intList):
        raise IndexError("Index is out of bounds for the input list")  # raises
    # an index error if idx is out of bounds

    intList.append(0)  # temporarily adds space towards end of list
    idx: int = len(intList) - 1  # then shifts everything over to the right for spacing

    while idx > addedIdx:  # iterates backwards until specified added idx position
        intList[idx] = intList[idx - 1]  # and shifts values over
        idx -= 1

    intList[addedIdx] = addedInt  # sets elem at the specified idx
