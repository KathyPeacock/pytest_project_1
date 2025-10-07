

import pytest
from lib.password_checker import *

# PasswordChecker returns True if the password entered is more than,
# or equal to 8 characters long.

# If the password isn't valid, an error is raised with a message.

def test_returns_true_for_valid_password():
    checker = PasswordChecker()
    result = checker.check("Nighttime")
    assert result is True


def test_returns_message_for_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        checker.check("Lol")
    assert str(err.value) == "Invalid password, must be 8+ characters."
    
def test_exactly_eight_character_password():
    checker = PasswordChecker()
    assert checker.check("12345678") == True

# Managed to make it a bit simpler in this above one, assert as True,
# rather than defining a result and asserting that as True in tw steps.


    