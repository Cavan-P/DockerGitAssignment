__author__ = "Cavan Pawlowski"
__date__ = "30 October, 2023"

import sys
from typing import List


def sumList(list: List[str]) -> int:
    sum: int = 0
    for i in list:
        sum += int(i)

    return sum


def roundAverage(n1: int, n2: int) -> int:
    return n1 // n2


def main() -> None:

    data = sys.stdin.readlines()

    n: str = data[0]
    values: List[str] = data[1].split(' ')

    print(roundAverage(sumList(values), int(n)))


if __name__ == "__main__":
    main()
