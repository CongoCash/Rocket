import random

class Vehicle(object):
    def __init__(self, color):
        self.speed = 0
        self.direction = 0
        self.color = color

    @staticmethod
    def random_car_color():
        colors = ['red', 'silver', 'yellow']
        return random.choice(colors)

color = Vehicle.random_car_color() # Static method returns a random color string
random_colored_vehicle = Vehicle(color=color) # Apply that string as an __init__() value
print random_colored_vehicle.color # Picks new color every time the program is interpreted