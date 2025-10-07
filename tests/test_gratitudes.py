
from lib.gratitudes import *

def test_initial_list_empty():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_add_single_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("Dani")
    assert gratitudes.gratitudes == ["Dani"]
    
def test_add_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Family")
    gratitudes.add("Nature")
    gratitudes.add("Books")
    assert gratitudes.gratitudes == ["Family", "Nature", "Books"]


def test_format_gratitudes_result():
    gratitudes = Gratitudes()
    gratitudes.add("Spirit")
    result = gratitudes.format()
    assert result == "Be grateful for: Spirit"