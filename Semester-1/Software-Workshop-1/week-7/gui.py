import tkinter as tk

app = tk.Tk()
app.title("Tkinter")
app.geometry("200x100+50+25")

button = tk.Button(app, text="Click me!")

button.pack()

app.mainloop()