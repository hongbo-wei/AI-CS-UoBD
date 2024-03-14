import random

random.seed(30)
print("first Number", random.randint(25, 50))

# generates a different random number
print("Second Number ", random.randint(25, 50))

# will generate a same random number as first one because seed value is same
random.seed(30)
print("Third Number", random.randint(25, 50))