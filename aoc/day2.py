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
