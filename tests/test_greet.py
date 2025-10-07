
from lib.greet import *

def test_greet():
    result = greet("Dani")
    assert result == f"Hello, Dani!"

    