def is_even(n):
    return n % 2 == 0

li = [1, 2, 3, 4, 5, 6]

new_li = list(filter(is_even, li))
print(new_li)

even_numbers = list(filter(lambda x: x % 2 == 0, li))
print(even_numbers)