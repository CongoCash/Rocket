def merge_sort(toSort):
    if len(toSort) <= 1:
        return toSort

    mIndex = len(toSort) / 2
    left = merge_sort(toSort[:mIndex])
    right = merge_sort(toSort[mIndex:])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if len(left) > 0:
        result.extend(merge_sort(left))
    else:
        result.extend(merge_sort(right))

    return result


items = [3,89,14,1,6,334,9,0,44,101]

print 'Before: ', items
merge_sort(items)
print 'After: ', items