def insertion_sort(items):
	for n in range(len(items)):
		i = n
		while i > 0 and items[i-1] > items[i]:
			items[i], items[i-1] = items[i-1], items[i]
			i -= 1




items = [3,89,14,1,6,334,9,0,44,101]

print 'Before: {}'.format(items)
insertion_sort(items)
print 'After: {}'.format(items)