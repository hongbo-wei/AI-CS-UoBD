def binary_search(arr, target, left=0, right=None):
  """
  Performs a binary search on a sorted array.

  Args:
      arr: The sorted array to search.
      target: The value to search for.
      left: The left index of the search space (default: 0).
      right: The right index of the search space (default: length of arr - 1).

  Returns:
      The index of the target in the array if found, otherwise -1.
  """
  if right is None:
      right = len(arr) - 1

  if left > right:
      return -1  # Target not found

  mid = (left + right) // 2

  if arr[mid] == target:
      return mid
  elif arr[mid] < target:
      return binary_search(arr, target, left=mid + 1, right=right)
  else:
      return binary_search(arr, target, left=left, right=mid - 1)

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print("Element is not present in array")
