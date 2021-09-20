import tkinter as tk
from tkinter import ttk


root = tk.Tk()


root.resizable(False, False)
root.title("Converter")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

meter_label = ttk.Label(root, text="Meter:")
meter_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

meter_entry = ttk.Entry(root)
meter_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

feet_label = ttk.Label(root, text="Feet:")
feet_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert")
convert_button.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

root.mainloop()
