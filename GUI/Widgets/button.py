import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Button")

ttk.Button(root, text="Press Me").pack()

root.mainloop()
