try:
    with open("week 7/lab/file_2.txt", 'r') as f:
        str = f.read()
        int = int(str)
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
