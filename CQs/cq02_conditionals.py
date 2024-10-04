"""A Number Guessing Gamem!"""

__author__ = "730758900"


def guess_a_number() -> None:
    secret: int = 7
    response: str = input("Guess a number: ")
    print("Your guess was " + response)

    if int(response) == secret:
        print("You got it!")
    elif int(response) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number
