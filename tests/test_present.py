
import pytest
from lib.present import *

# wrap stores the contents

def test_wrap_stores_contents():
    present = Present()
    present.wrap("dinosaur book")
    assert present.contents == "dinosaur book"

# unwrap returns contents

def test_unwrap_returns_contents():
    present = Present()
    present.wrap("dinosaur book")
    result = present.unwrap()
    assert result == "dinosaur book"

# unwrap raises correct error message if contents is None

def test_unwrap_raises_error_message_if_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."

# wrap raises correct error message if contents is not None

def test_wrap_raises_error_message_if_already_wrapped():
    present = Present()
    present.wrap("puppy")
    with pytest.raises(Exception) as e:
        present.wrap("guitar")
    assert str(e.value) == "A contents has already been wrapped."