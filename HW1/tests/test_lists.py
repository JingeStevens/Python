import pytest

from mypkg.my_answers import lists

p, r, c, d, o = lists()

def test_split():
    assert(p[0] == "Stevens")
    assert(p[1] == "is")
    assert(p[2] == "awesome")



