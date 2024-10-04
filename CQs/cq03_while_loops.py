"""Iterating over a string with a while loop"""

__author__ = "730758900"

def num_instances (phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while i < len(phrase) - 1:
        if search_char == phrase[i]:
            count += 1 
        i += 1 
    return count 
