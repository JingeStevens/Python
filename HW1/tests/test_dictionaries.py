import pytest

from mypkg.my_answers import dictionaries

a, f, p, k = dictionaries()


def test_fruit():
    assert(a == "apple")

