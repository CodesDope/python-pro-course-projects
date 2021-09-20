import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Check Box")

check_var = tk.StringVar()

ttk.Checkbutton(
    root, variable=check_var, onvalue="Checked", offvalue="Not Checked", text="Check Me"
).pack()

root.mainloop()
