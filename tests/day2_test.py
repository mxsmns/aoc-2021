import pytest

from aoc.data import get_input
from aoc.day2 import find_position


@pytest.mark.parametrize(
    ("data", "expected"),
    (
        pytest.param(
            ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"],
            (15, 10),
            id="example",
        ),
        pytest.param(get_input(2, "a"), (1991, 911), id="input"),
    ),
)
def test_part_a(data, expected):
    assert find_position(data) == expected
