import pytest

from mypkg.my_answers import numbers_and_strings

x, y, z, length, m, n = numbers_and_strings()


def test_power():
    assert(x == 4072324)

