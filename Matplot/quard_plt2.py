import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]

plt.plot(x, [i ** 2 for i in x], "ro")
plt.ylabel("Y - axis")
plt.xlabel("X - axis")
plt.show()
