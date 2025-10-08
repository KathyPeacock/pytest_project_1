

class House():

    def __init__(self, house_number, door_colour):
        self.floors = 2
        self.number = house_number
        self.door_colour = door_colour

    def repaint_door(self, new_colour):
        self.door_colour = new_colour
    
    def get_house_details(self):
        return f"House number {self.number} has {self.floors} floors and a {self.door_colour} door."
    

if __name__ == "__main__":
    my_house = House(42, "blue")
    print(my_house.get_house_details())

    dream_house = House(14, "lavender")
    print(dream_house.get_house_details())