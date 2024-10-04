"""Practice with Conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is less than 10"""
    if num < 10:
        print("Small number")
    else:
        print("Big Number")
    print("Have a nice day")


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter("happy", "h"))
