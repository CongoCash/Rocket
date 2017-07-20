class Vehicle(object):
    # General max speed for our vehicles
    max_speed = 100

    def __init__(self, color):
        self.speed = 0
        self.direction = 0
        self.color = color

    @classmethod
    def get_max_speed(cls):
        return cls.max_speed

class Boat(Vehicle):
    # Our boats are much slower
    max_speed = 60

print Vehicle.get_max_speed()  # Returns 100
print Boat.get_max_speed()  # Returns 60