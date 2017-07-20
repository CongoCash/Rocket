def merge(left, right):
	result = []
	left_counter = 0
	right_counter = 0
	while left_counter < len(left) and right_counter < len(right):
		if left[left_counter] <= right[right_counter]:
			result.append(left[left_counter])
			left_counter += 1
		else:
			result.append(right[right_counter])
			right_counter += 1

	if len(left) > 0:
		result.extend(left[left_counter:])
	if len(right) > 0:
		result.extend(right[right_counter:])
	return result


def merge_sort(lst):
	if len(lst) > 1:
		middle = len(lst) // 2
		left = lst[:middle]
		right = lst[middle:]

		left = merge_sort(left)
		right = merge_sort(right)

		return merge(left, right)

	return lst

items = [3,2,89,14,1,6,334,9,0,44,101]
print merge_sort(items)