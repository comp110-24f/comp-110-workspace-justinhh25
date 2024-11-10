"""Utility Functions with Dictionaries"""

__author__: str = "730758900"


def invert(input: dict[str, str]) -> dict[str, str]:
    keys: list[str] = []  # keys and values list instantiated in order to
    values: list[str] = []  # use the populated lists and invert them in the dict
    finalDict: dict[str, str] = {}  # empty dict created

    for keyElem in input:
        keys.append(keyElem)  # keys list is populated
        values.append(input[keyElem])  # values list is populated

    idx: int = 0
    while idx < len(keys):  # while index is less than length of keys list,
        if (
            values[idx] in finalDict
        ):  # if there are duplicates for values, which is keys in this case, error is raised
            raise KeyError("There are two duplicate keys in this dictionary")

        finalDict[values[idx]] = keys[
            idx
        ]  # values at index idx is assigned the key, and the key is assigned as value
        idx += 1  # while loop continues until len is reached

    return finalDict  # dictionary returned


def favorite_color(input: dict[str, str]) -> str:
    colorsCounterDict: dict[str, int] = {}  # dict defined
    colors: list[str] = []  # list for just the colors is defined

    for elem in input:
        colorName: str = input[elem]  # gives us the color keys in the input dict
        colors.append(colorName)  # appends those colorss keys into the colors list

        if (
            colorName in colorsCounterDict
        ):  # if that color is already in the dictionary, we increment it by 1
            colorsCounterDict[colorName] += 1
        else:
            colorsCounterDict[colorName] = 1  # if it isn't we assign it the value of 1

    idx: int = 0  # we use a while loop next to find the max frequency
    maxCount: int = (
        0  # idx is set to 0, maxcount is set to zero (can't have negative frequency)
    )
    mostColors: str = ""  # colors is set to blank in case so that it can be returned 

    while idx < len(colors):
        currentCount: int = colorsCounterDict[colors[idx]]  # gets the count of the current color in dictionary
        if currentCount > maxCount:  # if that count is greater, than mostColors gets that value of colors
            mostColors = colors[idx]  # and its maxCount is also set to the frequency of that color
            maxCount = currentCount
        idx += 1

    return mostColors  # color name is returned


def count(inputList: list[str]) -> dict[str, int]:
    finalDict: dict[str, int] = {}  # dictionary is instantiated with str keys and int values

    for elem in inputList:  # for each index in the input list, 
        if elem in finalDict:  # if the key is in the instantiated dict, we increment the value by 1
            finalDict[elem] += 1
        else:  # if the key is not in the in the dict, we assign it a value of 1
            finalDict[elem] = 1

    return finalDict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    finalDict: dict[str, list[str]] = {}  # final dict is instantiated

    for elem in input:  # for each element in the input list, we get its first character
        firstChar = elem[0].lower()

        if firstChar in finalDict:  # if that first character is already a key in the final dict, 
            finalDict[firstChar].append(elem)  # we can simply append it to the values of list strings
        else:
            finalDict[firstChar] = [elem]  # if it isn't a key already, then we instantiate it and assign it
            # with its corresponding word

    return finalDict


def update_attendance(
    inputDict: dict[str, list[str]], weekday: str, student: str
) -> None:
    if weekday in inputDict:  # if the weekday is already in the dictionary keys,
        if student not in inputDict[weekday]:  # and the student isn't there already, then we can simply append that student onto the list of strings
            inputDict[weekday].append(student)  #  we do this to check for duplicates and make sure the student doesn't get added twice
    else:  # but if the weekday isn't already there
        inputDict[weekday] = [student]  # we instantiate it with the keys as the weekday, and instantiate
        # a list of strings with the student's name

    return None
