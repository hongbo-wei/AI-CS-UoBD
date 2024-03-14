def binary_search_recursive(_arr, _target, _l, _r):
    if _l > _r:
        return -1

    M = (_l + _r) // 2
    mid_value = _arr[M]

    if mid_value == _target:
        return M
    elif mid_value < _target:
        return binary_search_recursive(_arr, _target, M + 1, _r)
    else:
        return binary_search_recursive(_arr, _target, _l, M - 1)

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 9
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print("Element found at index:" , result)  
else:
    print ("Element not found")