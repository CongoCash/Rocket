def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

items = [3,89,14,1,6,334,9,0,44,101]

print 'Before: ', items
insertion_sort(items)
print 'After: ', items