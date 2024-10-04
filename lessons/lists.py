"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)

my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

game_points: list[int] = [102, 86, 94]
print(game_points[2])

game_points[1] = 72
print(game_points)
print(len(game_points))
game_points.pop(1)
print(game_points)

# another example
# my_name: str = ""
# my_name: str = str()


def display(int_list: list[int]) -> None:
    counter: int = 0
    while counter < len(int_list):
        print(int_list[counter])
        counter += 1


display(game_points)
