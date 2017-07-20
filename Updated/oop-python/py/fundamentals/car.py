# Use a capital letter when defining a class
# The class name should also be singular (we have can only have one car at a time)
class Car(object):
	# Classes inherit from object because any new class you write will be a type of object

	# These variables are created when a new object is instantiated
	speed = 0
	direction = 0
	color = 'red'

# Instantiating a new car
new_car = Car()

# new_car is now a Car object stored in the computer's memory
print new_car


# Many classes uses an __init__() method to instantiate class instances.
# This allows you to define the attributes of the object when it is created (e.g. color), while still providing
# the option to have defaults (e.g. speed and direction)
class InitCar(object):

	# Self refers to the object being created. You do not pass self when actually using methods. Only when defining them
	def __init__(self, color='red'): # This makes the default color red
		self.speed = 0
		self.direction = 0
		self.color = color


class MethodCar(object):
	def __init__(self, color): # Now when the object is instantiated, the passed in color will be assigned to the color...i.e. car = Car('red')
		self.speed = 0
		self.direction = 0
		self.color = color

	def accelerat(self):
		self.speed += 1

	def brake(self):
		self.speed -= 1

	def turn_left(self):
		self.direction -= 90
