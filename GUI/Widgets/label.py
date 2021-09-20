import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Label")

ttk.Label(root, text="Hello", font=("Times New Roman", 14, "bold")).pack()
tk.Label(root, text="Different Text", bg="black", fg="#802bb1").pack()

tk.Label(root, text="New Line", bg="black", fg="#802bb1").pack(fill="x")

tk.Label(root, text="This is one more line", bg="green", fg="#802bb1").pack(
    fill="both", expand=True
)

root.mainloop()
