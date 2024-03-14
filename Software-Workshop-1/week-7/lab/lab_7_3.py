import datetime

while True:
    try:
        birth = int(input("Enter your birth year: "))
        current_year = datetime.datetime.now().year
        age = current_year - birth
        print(f"You age is {age}")
        break
    except ValueError as e:
        print("Please input a valid year")