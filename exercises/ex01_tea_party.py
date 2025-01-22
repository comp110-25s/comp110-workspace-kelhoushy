"""Program to determine number of treats, tea bags, and expected cost of a tea party 
based on an inputted number of guests"""

_author_: str = "730482808"


def main_planner(guests: int):
    """Prints number of teas, treats, and expected cost of the tea party"""
    print("A Cosy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags))
    print("Treats: " + str(treats))
    print("Cost: $" + str(cost))
    return None


def tea_bags(people: int) -> int:
    """Returns number of tea bags needed based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Returns number of treats needed based on number of guests"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns cost based on number of treats and teas"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "_main_":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
