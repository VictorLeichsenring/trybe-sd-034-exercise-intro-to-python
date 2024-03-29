from typing import List


def find_average(numbers: List[int]) -> float:
    soma = sum(numbers)
    return (soma/len(numbers))
