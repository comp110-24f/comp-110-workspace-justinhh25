__author__: str = "730758900"


def find_and_remove_max(input: list[int]) -> int:
    """Finds and removes instances of hte largest number in list"""
    if len(input) == 0:
        return -1

    maxValue: int = input[0]
    idx: int = 1
    idxPop: int = 0

    while idx < len(input):
        """Finds max value in the list"""
        currentValue: int = input[idx]
        if currentValue > maxValue:
            maxValue = currentValue
        idx += 1

    while idxPop < len(input):
        """Removes all instances of max value from list"""
        if maxValue == input[idxPop]:
            input.pop(idxPop)
            idxPop = -1
        idxPop += 1

    return maxValue
