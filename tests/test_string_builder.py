
from lib.string_builder import *

def test_inital_output_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""


def test_adding_a_string_outputs_same_string():
    string_builder = StringBuilder() 
    string_builder.add("Piece of string")
    assert string_builder.output() == "Piece of string"


def test_adding_a_string_sets_corresponding_string_size():
    string_builder = StringBuilder()
    string_builder.add("Piece of string")
    assert string_builder.size() == 15


def test_adding_multiple_strings_outputs_correct_concatenation():
    string_builder = StringBuilder()
    string_builder.add("How")
    string_builder.add(" ")
    string_builder.add("Long?")
    assert string_builder.output() == "How Long?"


def test_multiple_strings_correct_total_size():
    string_builder = StringBuilder()
    string_builder.add("How")
    string_builder.add(" ")
    string_builder.add("Long?")
    assert string_builder.size() == 9
    