"""EX02 - Chardle - A cute step towardw Wordle"""

__author__: str = "730758900"


def input_word() -> str:  # inputs for a word that has 5 characters
    response: str = input("Enter a 5-character word: ")
    if len(response) != 5:  # runs if the word doesn't have 5 characters
        print("Error: Word must contain 5 characters.")
        exit()  # exits the program to prevent it from running further
    return response  # returns the word


def input_letter() -> str:  # inputs for a single letter
    letter_response: str = input("Enter a single character: ")
    if len(letter_response) != 1:  # runs if the input isn't a single letter
        print("Error: Character must be a single character.")
        exit()  # exits the program to prevent it from running further
    return letter_response


def contains_char(
    word: str, letter: str
) -> None:  # takes in a word and letter and checks their indexes
    counter: int = 0  # counts how many instances of the character is found in a word
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:  # checks for a character in word at index 0
        print(letter + " found at index 0")
        counter += 1  # increments counter
    if word[1] == letter:  # checks for a character in word at index 1
        print(letter + " found at index 1")
        counter += 1  # increments counter
    if word[2] == letter:  # checks for a character in word at index 2
        print(letter + " found at index 2")
        counter += 1  # increments counter
    if word[3] == letter:  # checks for a character in word at index 3
        print(letter + " found at index 3")
        counter += 1  # increments counter
    if word[4] == letter:  # checks for a character in word at index 4
        print(letter + " found at index 4")
        counter += 1  # increments counter
    if counter == 0:  # runs if there are no instances of character in word
        print("No instances of " + letter + " found in " + word)
    elif counter == 1:  # runs if there is  one instance of character in word
        print(str(counter) + " instance of " + letter + " found in " + word)
    else:  # runs if there is more than one instance of character in word
        print(str(counter) + " instances of " + letter + " found in " + word)


def main() -> None:  # combines the functions together and allows it to be interacted
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # allows for the program to be ran
    main()
