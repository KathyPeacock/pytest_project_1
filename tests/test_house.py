
from lib.house import *

# check when we create a house it's given a house number
# and starting door colour, plus set attribute of 2 floors.

def test_house_initial_attributes():
    house = House(42, "blue")
    assert house.number == 42
    assert house.door_colour == "blue"
    assert house.floors == 2

# check repaint method changes attribute door_colour only

def test_repaint_door_changes_only_colour():
    house = House(42, "blue")
    house.repaint_door("pink")
    assert house.door_colour == "pink"
    assert house.number == 42
    assert house.floors == 2

# check get_house_details returns all details correctly
# and expected sentence 

def test_get_house_details_message():
    house = House(112, "orange")
    assert house.get_house_details() == "House number 112 has 2 floors and a orange door."