def string_scramble(str1, str2):
	# Sets are awesome: https://docs.python.org/2/library/sets.html
	str1_list = list(str1)
	str2_list = list(str2)
	for char in str2_list:
		if char in str1_list:
			del str1_list[str1_list.index(char)]
		else:
			return False
	return True
