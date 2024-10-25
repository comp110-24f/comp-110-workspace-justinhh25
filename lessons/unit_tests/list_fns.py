"""Three Functions to use on a list"""


def get_first(input: list[str]) -> str:
    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    firstVal: str = get_first(input)
    input.pop(0)
    return firstVal
