from typing import Sequence
from typing import Tuple


def find_position(commands: Sequence[str]) -> Tuple[int, int]:
    horizontal_position = 0
    depth = 0

    for command in commands:
        action, value = command.split()
        if action == "forward":
            horizontal_position += int(value)
        elif action == "up":
            depth -= int(value)
        elif action == "down":
            depth += int(value)
    return horizontal_position, depth


def find_position_with_aim(commands: Sequence[str]) -> Tuple[int, int]:
    horizontal_position = 0
    aim = 0
    depth = 0

    for command in commands:
        action, value = command.split()
        if action == "forward":
            horizontal_position += int(value)
            depth += aim * int(value)
        elif action == "up":
            aim -= int(value)
        elif action == "down":
            aim += int(value)
    return horizontal_position, depth
