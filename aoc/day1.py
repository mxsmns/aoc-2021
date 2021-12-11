from typing import Optional
from typing import Sequence

from aoc.data import get_input


def count_increasing_readings(readings: Sequence[float]) -> int:
    x = readings[0]
    num_increases = 0
    for y in readings[1:]:
        if y > x:
            num_increases += 1
        x = y
    return num_increases


def part_a() -> int:
    readings = [int(s) for s in get_input(1, "a")]
    return count_increasing_readings(readings)


def main(argv: Optional[Sequence[str]] = None) -> int:
    print(f"Part A solution: {part_a()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
