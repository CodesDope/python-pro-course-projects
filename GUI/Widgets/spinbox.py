import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Spinbox")


ttk.Spinbox(root, from_=0, to=5, wrap=False).pack()
ttk.Spinbox(root, from_=0, to=10, values=(0, 2, 4, 6, 8, 10), wrap=True).pack()

root.mainloop()
