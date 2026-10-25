import pytest

from src.calculator import calculate_average


def test_average_of_positive_numbers():
    assert calculate_average([2, 4, 6]) == 4


def test_average_of_negative_numbers():
    assert calculate_average([-2, -4, -6]) == -4


def test_average_of_single_number():
    assert calculate_average([5]) == 5


def test_empty_list_raises_error():
    with pytest.raises(ValueError):
        calculate_average([])