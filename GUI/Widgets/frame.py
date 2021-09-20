import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("600x300")
root.resizable(False, False)
root.title("Frame")

frame = ttk.Frame(root, width=200, height=200)

frame["padding"] = 5
frame["borderwidth"] = 2
frame["relief"] = "sunken"

frame.pack()

root.mainloop()
