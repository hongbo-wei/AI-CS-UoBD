def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        number *= factorial(number - 1)
        return number

print(factorial(5))
