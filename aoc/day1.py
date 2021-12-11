from typing import List
from typing import Optional
from typing import Sequence

from aoc.data import get_input


def count_increasing_readings(readings: Sequence[float], window: int = 1) -> int:
    num_increases = 0
    for i in range(len(readings) - window):
        x = readings[i : i + window]
        y = readings[i + 1 : i + 1 + window]
        if sum(y) > sum(x):
            num_increases += 1
    return num_increases


def part_a(readings: List[int]) -> int:
    readings = [int(s) for s in get_input(1, "a")]
    return count_increasing_readings(readings)


def part_b(readings: List[int]) -> int:
    return count_increasing_readings(readings, window=3)


def main(argv: Optional[Sequence[str]] = None) -> int:
    readings = [int(s) for s in get_input(1, "a")]
    print(f"Part A solution: {part_a(readings)}")
    print(f"Part A solution: {part_b(readings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
