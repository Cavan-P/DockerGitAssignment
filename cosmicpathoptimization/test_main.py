"""
Tests for main.py
"""

import unittest
from typing import List
from main import sumList


class TestMain(unittest.TestCase):

    def test_sumList1(self) -> None:
        values: List[str] = ['1', '2', '3', '4', '5']
        expectedSum: int = 15
        actualSum: int = sumList(values)

        self.assertEqual(expectedSum, actualSum)

    def test_sumList2(self) -> None:
        values: List[str] = ['5', '5', '5', '5']
        expectedSum: int = 20
        actualSum: int = sumList(values)

        self.assertEqual(expectedSum, actualSum)

    def test_sumList3(self) -> None:
        values: List[str] = ['0', '0', '0', '0', '1']
        expectedSum: int = 1
        actualSum: int = sumList(values)

        self.assertEqual(expectedSum, actualSum)

    def test_sumList4(self) -> None:
        values: List[str] = ['1']
        expectedSum: int = 1
        actualSum: int = sumList(values)

        self.assertEqual(expectedSum, actualSum)

    def test_sumList5(self) -> None:
        values: List[str] = ['10', '100', '50', '2', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1']
        expectedSum: int = 172
        actualSum: int = sumList(values)

        self.assertEqual(expectedSum, actualSum)

    def test_sumList6(self) -> None:
        values: List[str] = [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '9',
            '8',
            '7',
            '6',
            '5',
            '4',
            '3',
            '2',
            '1']
        expectedSum: int = 100
        actualSum: int = sumList(values)

        self.assertEqual(expectedSum, actualSum)


if __name__ == '__main__':
    unittest.main()
