import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]

plt.plot(x, [i ** 2 for i in x], "ro", x, [i ** 2 for i in x])
plt.ylabel("Y - axis")
plt.xlabel("X - axis")
plt.grid(True)
plt.text(1, 20, "Square Plot")
plt.title("Plot of Square")
plt.show()
