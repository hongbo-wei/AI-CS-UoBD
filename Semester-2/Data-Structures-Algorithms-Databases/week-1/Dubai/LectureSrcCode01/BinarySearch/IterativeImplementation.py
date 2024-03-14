def binary_search_iterative(_arr, _target):
    L = 0
    R = len(_arr) - 1

    while L <= R:
        M = (L + R) // 2
        mid_value = _arr[M]

        if mid_value == _target:
            return M
        elif mid_value < _target:
            L = M + 1
        else:
            R = M - 1
    return -1

arr = [1, 3, 5, 7, 9, 11]
target = 9
result = binary_search_iterative(arr, target)

if result != -1:
    print("Element found at index:" , result)  
else:
    print ("Element not found")