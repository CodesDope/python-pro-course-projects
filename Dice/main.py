import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from random import randint

root = tk.Tk()
root.geometry("200x200")
root.title("Dice")
root.resizable(False, False)

ttk.Button(
    root, text="Roll", command=lambda: showinfo(title="Dice", message=randint(1, 6))
).pack(expand=True, fill=tk.BOTH)

root.mainloop()
