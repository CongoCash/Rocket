# The Robots have discovered a new island and accidentally crashed on it. Tо survive, they need to create the largest rectangular
# field possible to make a landing strip. While surveying the land, they encountered a number of obstacles which they marked
# on their map. Each square of the map is marked according to whether it contains grass (G), rock (R), water (W), shrubs (S),
# or trees (T). While the grass can be mowed and the shrubs can be dug from the ground, the water, rocks, and trees cannot be
# removed with the tools at their disposal. Given these obstacles, they need your help to determine the area of the largest
# possible rectangular field.

# The island map is represented as a list of strings. Each string contains letter characters which indicate the conditions
# for each square of land (G, R, W, S, or T). The map is rectangular.

# Input: An island map as a list of strings.

# Output: The maximum area of the largest possible rectangle that can be cleared as an integer.

# Example:

# checkio(['G']) == 1
# checkio(['GS','GS']) == 4
# checkio(['GT','GG']) == 2
# checkio([
# 	'GGTGG',
# 	'TGGGG',
# 	'GSSGT',
# 	'GGGGT',
# 	'GWGGG',
# 	'RGTRT',
# 	'RTGWT',
# 	'WTWGR'
# 	]) == 9

# Precondition:
# 0 < len(landing_map) < 10
# all(0 < len(row) < 10 for row in landing_map)

def landing_strip(island_map):
	pass