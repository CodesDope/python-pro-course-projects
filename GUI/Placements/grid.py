import tkinter as tk

root = tk.Tk()
root.title("Grid")

root.geometry("600x300")

a = tk.Label(root, text="A", bg="#802bb1", fg="white")
b = tk.Label(root, text="B", bg="red", fg="white")
c = tk.Label(root, text="C", bg="green", fg="white")
d = tk.Label(root, text="D", bg="blue", fg="white")
e = tk.Label(root, text="E", bg="yellow", fg="black")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

a.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10)
b.grid(column=0, row=1, ipadx=10, ipady=10, padx=10, pady=10, sticky=tk.W)
c.grid(column=1, row=0, ipadx=10, ipady=10, padx=10, pady=10, sticky=tk.E)
d.grid(column=1, row=1, ipadx=10, ipady=10, padx=10, pady=10, sticky=tk.E)
e.grid(column=1, row=3, sticky=tk.EW)


root.mainloop()
