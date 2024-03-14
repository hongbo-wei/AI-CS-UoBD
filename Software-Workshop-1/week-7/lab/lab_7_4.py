import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()
        
        if operation == "Addition":
            result.set(num1 + num2)
        elif operation == "Subtraction":
            result.set(num1 - num2)
        elif operation == "Multiplication":
            result.set(num1 * num2)
        elif operation == "Division":
            result.set(num1 / num2)
    except ZeroDivisionError:
        result.set("Division by zero is not allowed")
    except ValueError:
        result.set("Invalid input. Please enter valid numbers.")
    
# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="white")

# Create and place input fields with black background and white foreground
label_num1 = tk.Label(window, text="Enter the first number:", bg="white", fg="black")
label_num1.pack()
entry_num1 = tk.Entry(window, bg="white", fg="black")
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter the second number:", bg="white", fg="black")
label_num2.pack()
entry_num2 = tk.Entry(window, bg="white", fg="black")
entry_num2.pack()

# Create and place operation dropdown with black background and white foreground
label_operation = tk.Label(window, text="Select an operation:", bg="white", fg="black")
label_operation.pack()
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
combo_operation = ttk.Combobox(window, values=operations, background="white", foreground="white")
combo_operation.set(operations[0])
combo_operation.pack()

# Create and place a calculate button with black background and white foreground
calculate_button = tk.Button(window, text="Calculate", command=calculate, bg="white", fg="black")
calculate_button.pack()

# Create and display the result with black background and white foreground
result = tk.StringVar()
result_text = tk.Label(window, text="Result: ", bg="white", fg="black")
result_text.pack()
result_label = tk.Label(window, textvariable=result, bg="white", fg="black")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
