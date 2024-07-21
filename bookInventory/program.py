def merge_sorted_arrays(a1, a2):
    n1 = len(a1)
    n2 = len(a2)
    i, j = 0, 0
    nums = []
    while i<n1 and j<n2:
        if a1[i]<=a2[j]:
            nums.append(a1[i])
            i += 1
        else:
            nums.append(a2[j])
            j += 1
    while i<n1:
        nums.append(a1[i])
        i = i + 1
    while j<n2:
        nums.append(a2[j])
        j += 1

    return nums

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    middle = len(arr) // 2
    left_side = merge_sort(arr[:middle])
    right_side = merge_sort(arr[middle:])


    return merge_sorted_arrays(left_side, right_side)


print(merge_sort([2, 3, 4, 5, 1]))
