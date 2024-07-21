
def selection_sort(nums):
    #write your code here
    n = len(nums)
    s = 0
    for i in range(n):
        j = i+1 
        while j < n:
            if nums[j] < nums[s]:
                s = j 
        nums[s], nums[i] = nums[i], nums[s]
        s = i
    return nums

print(selection_sort([3, 2, 5, 6]))
