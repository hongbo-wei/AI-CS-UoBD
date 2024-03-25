def binary_search(arr, num):
    # Initialize the left and right pointers
    left = 0
    right = len(arr) - 1
    # Loop through the array
    while left <= right:
        # Calculate the mid index
        mid = (left + right) // 2
        print(mid)
        # If the number is found, return the index
        if arr[mid] == num:
            return mid
        # If the number is less than the mid element, search the left half
        elif num < arr[mid]:
            right = mid - 1
        # If the number is greater than the mid element, search the right half
        else:
            left = mid + 1
    # If the number is not found, return -1
    return -1

arr = [10, 15, 18, 19, 22, 25, 28, 30]

index = binary_search(arr, 22)
print(index)