"""Tea party planner that calculates treats/tea bags needed, and cost of party"""

__author__: str = "730758900"


def main_planner(guests: int) -> None:
    """Brings all functions together and produces a printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # values with int data type must be converted to string to be concatenated
    print("Tea Bags: " + str(tea_bags(guests)))
    # need to call tea bag function to get amount of tea bags
    print("Treats: " + str(treats(guests)))
    # need to call treat function to get amount of treats
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # total cost is found by calling tea bags and treats function


def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed"""
    return people * 2
    # number of tea bags is equal to the amount of people multiplied by 2


def treats(people: int) -> int:
    """Computes number of treats needed based on number of tea guests drink"""
    return int((1.5) * tea_bags(people=people))
    # number of treats is reliant upon amount of tea bags times 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """Computes cost of tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)
    # each tea bag is worth 50 cents, each treat is worth 75 cents.
    # multiplying and taking the sum gets us total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # allows this program to have some sort of interaction and be able to run
