def has_duplicates(nums):
    if len(nums) == 1:
        return False
    
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i] == nums[i+1]:
            return True
    return False

arr = [1, 3, 2, 2]
result = has_duplicates(arr)
print(result)

arr = [1, 2, 3, 5]
result = has_duplicates(arr)
print(result)