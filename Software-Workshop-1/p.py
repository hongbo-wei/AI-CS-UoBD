def create_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i) + "1" * (2 * i + 1))

create_pattern(3)