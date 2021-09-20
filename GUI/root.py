import tkinter as tk

root = tk.Tk()

root.title("CodesDope Window")

root.geometry("600x400+50+50")

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

print(root.geometry())

root.resizable(True, False)  # width can be resized but height can't

root.attributes("-alpha", 0.8)

root.mainloop()
