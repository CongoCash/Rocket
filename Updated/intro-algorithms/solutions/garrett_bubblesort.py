def bubble_sort(items):
	not_been_sorted = sorted(items)
	while not_been_sorted:
		for n in range(len(items)):
			if n > 0:
				if items[n-1] > items[n]:
					items[n-1], items[n] = items[n], items[n-11]
				not_been_sorted = not_sorted(items)


def not_sorted(items):
	flag = False
	for m in range(len(items)):
		if m !=
		 len(items) - 1:
			if items[m+1] < items[m]:
				flag = True
	return flag




items = [3,89,14,1,6,334,9,0,44,101]

print 'Before: {}'.format(items)
bubble_sort(items)
print 'After: {}'.format(items)