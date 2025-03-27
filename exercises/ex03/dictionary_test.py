"""My fourth exercise in COMP110!"""

__author__ = "730660220"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

# Tests for invert


def KeyError_Test():
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_invert():
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single():
    assert invert({"apple": "cat"}) == {"cat": "apple"}


# Tests for count


def testCount():
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def testCount_empty():
    assert count([]) == {}


def testCount_mult():
    assert count(["x", "y", "x", "z", "z", "z"]) == {"x": 2, "y": 1, "z": 3}


# Tests for favorite_color


def testFavcolor():
    data = {"Alice": "blue", "Bob": "green", "Charlie": "blue"}
    assert favorite_color(data) == "blue"


def testFavcolor_tie():
    data = {"Alice": "red", "Bob": "blue", "Charlie": "red", "Dana": "blue"}
    assert favorite_color(data) == "red"


def testFavcolor_empty():
    assert favorite_color({}) == ""


# Tests for bin_len


def test_binlen():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_binlen_duplicates():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_binlen_empty():
    assert bin_len([]) == {}
