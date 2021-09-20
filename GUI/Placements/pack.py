import tkinter as tk

root = tk.Tk()
root.title("Pack")

root.geometry("600x300")

a = tk.Label(root, text="A", bg="#802bb1", fg="white")
b = tk.Label(root, text="B", bg="red", fg="white")
c = tk.Label(root, text="C", bg="green", fg="white")
d = tk.Label(root, text="D", bg="blue", fg="white")
e = tk.Label(root, text="E", bg="yellow", fg="black")

f = tk.Label(root, text="F", bg="red", fg="black")
g = tk.Label(root, text="G", bg="green", fg="black")
h = tk.Label(root, text="H", bg="white", fg="black")


a.pack(ipadx=10, ipady=10)
b.pack(padx=10, pady=10, fill="x")
c.pack(ipadx=10, ipady=10, fill="both", expand=True)
d.pack(ipadx=10, ipady=10, side="right")
e.pack(ipadx=10, ipady=10, side="left")

f.pack(fill="both", side="left", expand=True)
g.pack(fill="both", side="left", expand=True)
h.pack(fill="both", side="left", expand=True)

root.mainloop()
