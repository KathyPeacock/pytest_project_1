
from lib.report_length import *

def test_report_length():
    assert report_length("Cheese") == "This string was 6 characters long."


def test_report_length_for_long_string():
    assert report_length("Hello, I really like cheese...") == "This string was 30 characters long."

# NB: the message the user recieves uses the terminology characters, which might be confusing 
# for users who don't know Pythonic way of indexing to include spaces etc.

def test_report_length_for_short_string():
    assert report_length("Me") == "This string was 2 characters long."


def test_report_length_for_empty_string():
    assert report_length("") == "This string was 0 characters long."

def test_report_length_for_string_of_spaces_only():
    assert report_length("  ") == "This string was 2 characters long."