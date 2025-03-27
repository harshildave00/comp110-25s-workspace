"""My second exercise in COMP110!"""

__author__ = "730660220"


def main_planner(guests: int) -> None:
    """The entrypoint of the program that calls each other functions."""

    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea bags needed: {tea_bags(guests)}")
    print(f"Treats needed: {treats(guests)}")
    print(f"Total cost: ${cost(tea_bags(guests), treats(guests)):.1f}")


def tea_bags(people: int) -> int:
    """Returns the number of tea bags needed for a tea party."""
    return people * 2


def treats(people: int) -> int:
    """Computes number of treats based on total_teas."""
    total_teas = tea_bags(people=people)
    total_treats = total_teas * 1.5
    return int(total_treats)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and the treats combined"""
    cost_tea = tea_count * 0.50
    cost_treat = treat_count * 0.75
    total_cost = cost_tea + cost_treat
    return total_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
