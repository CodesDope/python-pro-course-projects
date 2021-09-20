import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")
root.title("Radio Button")

radio_var = tk.StringVar()

ttk.Radiobutton(root, text="S", value="s", variable=radio_var).pack(fill="x")
ttk.Radiobutton(root, text="M", value="m", variable=radio_var).pack(fill="x")
ttk.Radiobutton(root, text="L", value="l", variable=radio_var).pack(fill="x")

root.mainloop()
