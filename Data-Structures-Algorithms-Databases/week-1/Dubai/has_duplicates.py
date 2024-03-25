'''
Overall time complexity is O(n*n) because we have a nested loop.
'''
def has_duplicates(nums):
    seen_elements = []
    for num in nums: # O(n)
        if num in seen_elements: # O(n)
                return True
        seen_elements.append(num)
    return False

arr = [1, 3, 2, 2]
result = has_duplicates(arr)
print(result)

arr = [1, 2, 3, 5]
result = has_duplicates(arr)
print(result)