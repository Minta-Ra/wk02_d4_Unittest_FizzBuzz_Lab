import unittest
from src.fizzbuzz import *


class TestFizzbuzz(unittest.TestCase):

    def test_fizz_buzz__3_returns_fizz(self):
        expected = "Fizz"
        actual = fizz_buzz(3)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__5_returns_buzz(self):
        expected = "Buzz"
        actual = fizz_buzz(5)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__15_returns_fizzbuzz(self):
        expected = "FizzBuzz"
        actual = fizz_buzz(15)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__0_returns_0(self):
        expected = "0"
        actual = fizz_buzz(0)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__7_returns_7(self):
        expected = "7"
        actual = fizz_buzz(7)
        self.assertEqual(expected, actual)

    def test_list_sequence__count_0_to_15(self):
        expected = [
            "0",
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
        actual = list_sequence(15)
        self.assertEqual(expected, actual)