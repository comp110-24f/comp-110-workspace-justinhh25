"""Concatenates two string variables together"""

__author__ = "730758900"

word1: str = "happy"
word2: str = "tuesday"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


if __name__ == "__main__":
    print(concat(word1, word2))
