from typing import List


def find_biggest_name(names: List[str]) -> str:
    return max(names, key=len)
