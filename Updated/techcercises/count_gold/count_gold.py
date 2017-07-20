# Consider a tuple of tuples in which the first tuple has one integer and each consecutive tuple has one more integer
# then the last. Such a tuple of tuples would look like a triangle. You should write a program that will help find
# the highest possible sum on the most profitable route down the pyramid.
# All routes down the pyramid involve stepping down and to the left or down and to the right.

# Tips: Think of each step down to the left as moving to the same index location or to the right as one index
# location higher. Be very careful if you plan to use recursion here.


# Example:

# count_gold((
#     (1,),
#     (2, 3),
#     (3, 3, 1),
#     (3, 1, 5, 4),
#     (3, 1, 3, 1, 3),
#     (2, 2, 2, 2, 2, 2),
#     (5, 6, 4, 5, 6, 4, 3)
# )) == 23

# count_gold((
#     (1,),
#     (2, 1),
#     (1, 2, 1),
#     (1, 2, 1, 1),
#     (1, 2, 1, 1, 1),
#     (1, 2, 1, 1, 1, 1),
#     (1, 2, 1, 1, 1, 1, 9)
# )) == 15

# count_gold((
#     (9,),
#     (2, 2),
#     (3, 3, 3),
#     (4, 4, 4, 4)
# )) == 18


# Precondition: 0 < len(pyramid) ≤ 20
from copy import deepcopy


def count_gold(pyramid):
    result = []
    for i in pyramid[::-1]: # Bottom up
	# A deep copy constructs a new compound object
	# and then, recursively, inserts copies into it of the objects found in the original.
        temp_result = deepcopy(list(i))
        if not result:
            result = deepcopy(temp_result)
            continue
        for j in range(len(temp_result)):
            temp_result[j] = temp_result[j] + max(result[j], result[j + 1])
        result = deepcopy(temp_result)
    return max(result)

