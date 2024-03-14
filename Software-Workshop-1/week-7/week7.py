'''
# This is a global variable
x = "global"

def func():
    # The function can access the global variable
    print("x inside:", x)

func()
print("x outside:", x)

# *****************************

def func():
    # This is a local variable
    y = "local"
    print("y inside:", y)

func()
# This will cause an error because y is not accessible outside the function
# print("y outside:", y)

# *****************************

z = "global z"

def func():
    z = "local z"
    print("z inside:", z)

func()
print("z outside:", z)

# *****************************
a = "global a"

def func():
    global a
    a = "modified a"
    print("a inside:", a)

func()
print("a outside:", a)
# *****************************
# Incorrect logic for finding the maximum value in a list
def find_max(values):
    max_value = 0
    for value in values:
        if value > max_value:  # This should be 'value > max_value'
            max_value = value
    return max_value

# The function can be tested using assertions or unit tests
assert find_max([1, 2, 3, 4, 5]) == 5, "The function did not return the correct max value"
# *****************************

a = 5
b = 2

print (a/b)
# *****************************
a = 5
b = 2

print (a/b)

print ("Bye")
# *****************************
a = 5
b = 0

print (a/b)

print ("Bye")

# *****************************
a = 5 #normal statment 
b = 0
try:
  print (a/b) #critical statment 
except Exception:
  print ("you can not divied by zero")

print ("Bye")
# *****************************
from os.path import expanduser
a = 5 #normal statment 
b = 2
try:
  print (a/b) #critical statment 
except Exception:
  print ("you can not divied by zero")

print ("Bye")

# *****************************
#https://docs.python.org/3/library/exceptions.html

a = 5 #normal statment 
b = 0
try:
  print (a/b) #critical statment 
except Exception as e:
  print ("you can not divied by zero", e)

print ("Bye")
# *****************************
a = 5 #normal statment 
b = 0
try:
  print ("Resource open")
  print (a/b) #critical statment 
  print ("Resource closed")
except Exception as e:
  print ("you can not divied by zero", e)

print ("Bye")
# *****************************
a = 5 #normal statment 
b = 0
try:
  print ("Resource open")
  print (a/b) #critical statment 
  
except Exception as e:
  print ("you can not divied by zero", e)
  print ("Resource closed")

print ("Bye")
# *****************************



a = 5 #normal statment 
b = 2
try:
  print ("Resource open")
  print (a/b) #critical statment 
  
except Exception as e:
  print ("you can not divied by zero", e)
  print ("Resource closed")

print ("Bye")
# *****************************



a = 5 #normal statment 
b = 2
try:
  print ("Resource open")
  print (a/b) #critical statment 
  
except Exception as e:
  print ("you can not divied by zero", e)

finally:
  print ("Resource closed")

print ("Bye")


a = 5 #normal statment 
b = 2
try:
  print ("Resource open")
  print (a/b) #critical statment 
  k= int(input("Enter a number "))
  print (k)
  
except Exception as e:
  print ("you can not divied by zero", e)

finally:
  print ("Resource closed")

print ("Bye")
# *****************************



a = 5 #normal statment 
b = 2
try:
  print ("Resource open")
  print (a/b) #critical statment 
  k= int(input("Enter a number "))
  print (k)
  
except Exception as e:
  print ("you can not divied by zero", e)

finally:
  print ("Resource closed")

print ("Bye")


# *****************************


a = 5 #normal statment 
b = 2
k= int(input("Enter a number "))
print (k)

try:
  print ("Resource open")
  print (a/b) #critical statment 
  
  
except Exception as e:
  print ("you can not divied by zero", e)

finally:
  print ("Resource closed")

print ("Bye")

# *****************************


a = 5 #normal statment 
b = 2

try:
  print ("Resource open")
  print (a/b) #critical statment 
  k= int(input("Enter a number "))
  print (k)

  
  
except ZeroDivisionError as e:
  print ("you can not divied by zero", e)

except ValueError as e:
  print ("invialid inour", e)

except Exception as e:
  print ("something wnet err", e)

finally:
  print ("Resource closed")

print ("Bye")

# *****************************



import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = var_operation.get()

        if operation == 'addition':
            result = num1 + num2
        elif operation == 'subtraction':
            result = num1 - num2
        elif operation == 'multiplication':
            result = num1 * num2
        elif operation == 'division':
            result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields for numbers
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Dropdown menu for operation
var_operation = tk.StringVar(root)
var_operation.set("addition")  # default value

label_operation = tk.Label(root, text="Choose an operation:")
label_operation.pack()

option_operation = tk.OptionMenu(root, var_operation, "addition", "subtraction", "multiplication", "division")
option_operation.pack()

# Button to calculate
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

# Label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Run the application
root.mainloop()




'''
