try:
   f = open("week 7/lab/file_2.txt", 'r')
except FileNotFoundError as e:
    print("File not found")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Ensure that the file is closed, whether an exception occurred or not
    if 'f' in locals() and not f.closed:
        f.close()
        print("File has been closed.")