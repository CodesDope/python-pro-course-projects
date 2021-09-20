import tkinter as tk

root = tk.Tk()
root.title("Place")

root.geometry("600x300")

a = tk.Label(root, text="A", bg="#802bb1", fg="white")
b = tk.Label(root, text="B", bg="red", fg="white")
c = tk.Label(root, text="C", bg="green", fg="white")
d = tk.Label(root, text="D", bg="blue", fg="white")
e = tk.Label(root, text="E", bg="yellow", fg="black")

a.place(x=10, y=10)
b.place(relx=0.5, rely=0.1, relwidth=0.3)
c.place(relx=0.1, rely=0.1, relwidth=0.5, anchor="w")

root.mainloop()
