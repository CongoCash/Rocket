def quick_sort(items):
	less = []
	equal = []
	greater = []

	if len(items) > 1:
		pivot_index = len(items) / 2
		pivot = items[pivot_index]
		for item in items:
			# Put each item in their appropriate bin
			if item < pivot:
				less.append(item)
			if item == pivot:
				equal.append(item)
			if item > pivot:
				greater.append(item)
		# make a recursive call on each respective bin and let recursion take over
		return quick_sort(less) + equal + quick_sort(greater)
	return items



items = [3,89,14,1,6,5,334,9,0,44,101]

print 'Before: ', items
q = quick_sort(items)
print 'After: ', q
