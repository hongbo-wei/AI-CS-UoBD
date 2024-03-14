def linear_search(_arr, _target):
    for i in range(len(_arr)):
        if _arr[i] == _target:
            return i
    return -1

myArray = [20, 15, 10, 50, 16, 18, 18]
searchTarget = 18
result = linear_search(myArray, searchTarget)

if result != -1:
    print("Element found at index:" , result)  
else:
    print ("Element not found")