def linear_search(arr, num):
    # Loop through the array
    for i in range(len(arr)):
        # If the number is found, return the index
        if arr[i] == num:
            return i
    # If the number is not found, return -1
    return -1

arr = [20, 15, 10, 50, 16, 18, 18]

index = linear_search(arr, 18)

print(index)