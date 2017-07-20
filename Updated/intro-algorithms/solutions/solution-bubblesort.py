def bubble_sort(items):

    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


items = [3,89,14,1,6,334,9,0,44,101]

print 'Before: ', items
bubble_sort(items)
print 'After: ', items