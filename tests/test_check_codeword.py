

from lib.check_codeword import *

def test_correct_match_returns_success():
    assert check_codeword("horse") == "Correct! Come in."

def test_starts_with_h_ends_with_e_but_not_horse_returns_close():
    assert check_codeword("hare") == "Close, but nope."

def test_other_words_return_fail():
    assert check_codeword("railway") == "WRONG!"

    