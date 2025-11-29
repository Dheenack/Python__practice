# run by  $>pytest name.py
import pytest
from my_code import add

# Parametrize decorator
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_parametrize(a, b, expected):
    assert add(a,b) == expected
