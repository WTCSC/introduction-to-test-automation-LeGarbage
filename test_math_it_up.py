import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  assert math_it_up.is_even(2)
  assert math_it_up.is_even(0)
  assert not math_it_up.is_even(1)
  assert not math_it_up.is_even(-1)
  assert math_it_up.is_even(-2)
  assert math_it_up.is_even(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999998)

def test_is_odd():
  assert not math_it_up.is_odd(2)
  assert not math_it_up.is_odd(0)
  assert math_it_up.is_odd(1)
  assert math_it_up.is_odd(-1)
  assert not math_it_up.is_odd(-2)
  assert math_it_up.is_odd(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

def test_mean():
  assert math_it_up.mean([i for i in range(1, 101)]) == 50.5
  assert math_it_up.mean([i for i in range(-2, 3)]) == 0
  assert math_it_up.mean([69 for i in range(69)]) == 69

def test_median():
  assert math_it_up.median([i for i in range(1, 100)]) == 50
  assert math_it_up.median([i for i in range(1, 101)]) == 50.5
  assert math_it_up.mean([69 for i in range(69)]) == 69

def test_mode():
  assert math_it_up.mode([69 for i in range(69)].append(0)) == [69]
  assert math_it_up.mode([i for i in range(1, 101)]) == [i for i in range(1, 101)]
  assert math_it_up.mode([i for i in range(-100, 1000)].append(0)) == [0]