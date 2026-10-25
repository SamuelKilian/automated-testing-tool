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

@pytest.mark.parametrize(
    "values, expected",
    [
        ([2, 4, 6], 4),
        ([-2, -4, -6], -4),
        ([5], 5),
        ([0, 0, 0], 0),
        ([1, 2], 1.5),
        ([1.5, 2.5], 2.0),
    ],
)
def test_average_with_multiple_inputs(values, expected):
    assert calculate_average(values) == pytest.approx(expected)