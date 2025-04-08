"""COMP 110 Exercise 03: Dictionary"""

__author__ = "730482808"

from dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_use_1() -> None:
    """One use case test for invert function"""
    assert invert({"run": "ran", "swim": "swam", "dive": "dove"}) == {
        "ran": "run",
        "swam": "swim",
        "dove": "dive",
    }


def test_invert_use_2() -> None:
    """Second use case test for invert function"""
    assert invert({"car": "race", "bat": "man"}) == {"race": "car", "man": "bat"}


def test_invert_edge() -> None:
    """Edge case for invert function, results in KeyError"""
    with pytest.raises(KeyError):
        fruits = {"apples": "oranges", "tangerines": "oranges"}
        invert(fruits)


def test_count_use_1() -> None:
    """One use case test for count function"""
    assert count(["Banana", "Mango", "Cherry", "Mango"]) == {
        "Banana": 1,
        "Mango": 2,
        "Cherry": 1,
    }


def test_count_use_2() -> None:
    """Second use case test for count function"""
    assert count(["fruit", "fruit", "fruit", "fruit"]) == {"fruit": 4}


def test_count_edge() -> None:
    """Edge case for count function with an empty value"""
    assert count(["fruit", "fruit", "fruit", ""]) == {"fruit": 3, "": 1}


def test_favorite_color_use_1() -> None:
    """One use case test for favorite_color function"""
    assert (
        favorite_color({"Mark": "Yellow", "Steve": "Blue", "Lisa": "Yellow"})
        == "Yellow"
    )


def test_favorite_color_use_2() -> None:
    """Second use case test for favorite_color function"""
    assert (
        favorite_color(
            {"Mark": "Yellow", "Steve": "Blue", "Lisa": "Yellow", "Grace": "Blue"}
        )
        == "Yellow"
    )


def test_favorite_color_edge() -> None:
    """Edge case for favorite_color function with empty values"""
    assert favorite_color({"Mark": "", "Steve": "Blue", "Lisa": ""}) == ""


def test_bin_len_use_1() -> None:
    """One use case test for bin_len function"""
    assert bin_len(["base", "basket", "foot"]) == {4: {"base", "foot"}, 6: {"basket"}}


def test_bin_len_use_2() -> None:
    """Second use case test for bin_len function"""
    assert bin_len(["code"]) == {4: {"code"}}


def test_bin_len_edge() -> None:
    """Edge case for bin_len function with empty values"""
    assert bin_len(["", "", "done"]) == {0: {""}, 4: {"done"}}
