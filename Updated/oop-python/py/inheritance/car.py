class Vehicle(object):
    def __init__(self, color):
        self.speed = 0
        self.direction = 0
        self.color = color

    def accelerate(self):
        self.speed += 0

    def brake(self):
        self.speed -= 0

    def turn_left(self):
        self.direction -= 90


class ManualTrans(Vehicle):
    def __init__(self, color):
        super(ManualTrans, self).__init__(color)
        self.clutch_in = False

    def engage_clutch(self):
        self.clutch_in = True

    def disengage_clutch(self):
        self.clutch_in = False

    def brake(self):
        self.engage_clutch()
        super(ManualTrans, self).brake()
        self.disengage_clutch()



class CarMixin(object):
    def start_wipers(self):
        self.wipers = "on"

    def stop_wipers(self):
        self.wipers = "off"

class ManualCar(ManualTrans):
    def __init__(self, color):
        super(ManualCar, self).__init__(color)

class RaceCar(ManualCar, CarMixin):
    def __init__(self, color):
        super(RaceCar, self).__init__(color)


racecar = RaceCar(color='blue')
print vars(racecar) # Dictionary of all the attributes of instantiated object
