import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Entry")

entry_var = tk.StringVar()

ttk.Entry(root, textvariable=entry_var).pack()
ttk.Entry(root, show="*").pack()

root.mainloop()
