"""A Replica of the game Wordle!"""

__author__ = "730758900"

# creates the global variables for emojis used
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(numChars: int) -> str:
    """Checks if the response matches the number of chars in secret"""
    response: str = input(
        f"Enter a {numChars} character word: "
    )  # gathers guess for a char amount of words
    while len(response) != numChars:  # ensures right amount of chars is inputted
        response = input(f"That wasn't {numChars} chars! Try again: ")
    return response


def contains_char(
    searchWord: str, searchChar: str
) -> bool:  # checks to see whether the char guessed is in the secret word
    """Searches for a character in the provided word"""
    assert len(searchChar) == 1
    idxChars: int = 0
    while idxChars < len(searchWord):  # while loop to iterate through secret word
        if searchWord[idxChars] == searchChar:
            return True  # is returned True if char is found in secret word
        idxChars += 1
    return False  # if not found, return False


def emojified(
    guessWord: str, secretWord: str
) -> str:  # this function prints out our results in emojis
    """Compares char indexes with secret word and returns emoji based on result"""
    assert len(guessWord) == len(secretWord)
    emojis: str = ""  # no emojis so far
    idxEmoji: int = 0
    while idxEmoji < len(
        secretWord
    ):  # while loop iterates chars in guessWord with secretWord
        if (
            guessWord[idxEmoji] == secretWord[idxEmoji]
        ):  # if chars are in same index, return green
            emojis += GREEN_BOX
        elif contains_char(
            secretWord, guessWord[idxEmoji]
        ):  # if chars are in the word, return yellow
            emojis += YELLOW_BOX
        else:  # if no chars are found at all, return white
            emojis += WHITE_BOX
        idxEmoji += 1
    return emojis  # prints out emoji results


def main(
    secret: str,
) -> None:  # allows us to create a game based on any word we specify in "secret"
    """Entrypoint of the program and main game loop"""
    turns: int = 1  # starts out with one turn
    maxTurns: int = 6  # only allowed 6 turns
    while turns <= 6:  # iterates through the game loop as long as it is within 6 turns
        print(f"=== Turn {turns}/{maxTurns} ===")
        guesses = input_guess(
            numChars=len(secret)
        )  # responses are recorded in "guesses" and are checked to see if right amount of chars is reached
        print(
            emojified(guessWord=guesses, secretWord=secret)
        )  # turns the guesses into emojis and prints it out

        if (
            guesses == secret
        ):  # if the guess is equal to the secret word, the game is won
            print(f"You won in {turns}/{maxTurns} turns!")
            return
        turns += 1

    print(
        f"X/{maxTurns} - Sorry, try again tomorrow!"
    )  # once turns has gone over 6, the defeat statement is printed


if __name__ == "__main__":
    main(secret="codes")
