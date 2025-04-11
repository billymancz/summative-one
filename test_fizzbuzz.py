import pytest
from fizzbuzz import fizzbuzz

def test_fizzbuzz_returns_number():
    assert fizzbuzz(1) == "1"

def test_fizzbuzz_returns_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz_returns_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_fizz_returns_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"