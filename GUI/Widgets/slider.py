import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Slider")

curr_value = tk.DoubleVar()

ttk.Scale(root, from_=0, to=10, orient="horizontal", variable=curr_value).pack()

root.mainloop()
