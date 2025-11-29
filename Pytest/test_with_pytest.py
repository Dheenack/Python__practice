## run by $>pytest name.py
import pytest
from my_code import add

@pytest.fixture
def sample_data():
    return {"a": 5, "b": 3}

def test_add_with_fixture(sample_data):
    result = add(sample_data["a"], sample_data["b"])
    assert result == 8
