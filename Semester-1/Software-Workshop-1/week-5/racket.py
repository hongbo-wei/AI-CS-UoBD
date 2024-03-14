import random


rate_1 = 0.4
rate_2 = 1 - rate_1
winner_1 = 0
winner_2 = 0

for i in range(10):
    random_number = random.random()
    print(random_number)
    if random_number < rate_1 or random_number == rate_1:
        winner_1 += 1
    else:
        winner_2 += 1

print(f"Winner 1 wins: {winner_1}")
print(f"Winner 2 wins: {winner_2}")