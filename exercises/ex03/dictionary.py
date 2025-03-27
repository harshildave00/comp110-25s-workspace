"""My fourth exercise in COMP110!"""

__author__ = "730660220"


def invert(new_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values of the dictionary that is inputted"""
    inverted_dictionary = {}
    for key, value in new_dict.items():
        if value in inverted_dictionary:
            raise KeyError(f"Duplicate key detected: '{value}' is already a key.")
        inverted_dictionary[value] = key
    return inverted_dictionary


def count(list_values: list[str]) -> dict[str, int]:
    """Returns a dict showing how frequently each unique value appears in the list."""
    empty_dict: dict[str, int] = {}
    for item in list_values:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently"""
    colorCount = count(list(favorites.values()))

    maximum_count = 0
    most_frequent = ""

    for color in colorCount:
        if colorCount[color] > maximum_count:
            maximum_count = colorCount[color]
            most_frequent = color
        elif colorCount[color] == maximum_count and most_frequent == "":
            most_frequent = color

    return most_frequent


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins strings by length into a dict containing words of the same length."""
    resulting_dict: dict[int, set[str]] = {}
    for word in words:
        str_length = len(word)
        if str_length in resulting_dict:
            resulting_dict[str_length].add(word)
        else:
            resulting_dict[str_length] = {word}
    return resulting_dict
