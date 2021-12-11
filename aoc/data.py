import os
from typing import List
from typing import Literal


def get_input(
    day: int,
    part: Literal["a", "b"],
) -> List[str]:
    input_folder = os.path.join(__file__, os.path.pardir, "inputs")

    input_file = os.path.abspath(
        os.path.join(input_folder, f"day_{day}", f"part_{part}.txt")
    )

    with open(input_file) as f:
        contents = f.read().strip()

    return contents.split("\n")
