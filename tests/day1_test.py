import pytest

from aoc.data import get_input
from aoc.day1 import count_increasing_readings


@pytest.mark.parametrize(
    ("data", "expected"),
    (
        pytest.param(
            [
                199,
                200,
                208,
                210,
                200,
                207,
                240,
                269,
                260,
                263,
            ],
            7,
            id="example",
        ),
        pytest.param([int(s) for s in get_input(1, "a")], 1692, id="input"),
    ),
)
def test_part_a(data, expected):
    assert count_increasing_readings(data) == expected
