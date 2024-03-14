from functools import reduce

li = [6, 6, 6, 6, 6, 7]

a = reduce(lambda x, y: x +y, li) / len(li)

print(a)

