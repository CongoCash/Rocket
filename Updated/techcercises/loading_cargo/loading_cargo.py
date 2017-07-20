# Input data: A list of the weights as a list of integers.

# Output data: The number representing the lowest possible weight difference as a positive integer.

# Example:

# checkio([10,10]) == 0
# checkio([10]) == 10
# checkio([5, 8, 13, 27, 14]) == 3
# checkio([5,5,6,5]) == 1
# checkio([12, 30, 30, 32, 42, 49]) == 9
# checkio([1, 1, 1, 3]) == 0

# How it is used: This is a combinatorial optimization version of the partition problem. The combinatorial optimization has wide
# usage and you often see it when you look at automated schedules or route calculating.

# Precondition:
# 0 < len(weights) ≤ 10
# all(0 < x < 100 for x in weights)

def loading_cargo(lst):
	pass