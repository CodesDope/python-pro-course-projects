import matplotlib.pyplot as plt

x = [x * 0.1 for x in range(0, 10)]

plt.plot(x, x, "r--", x, [i ** 2 for i in x], "bs", x, [i ** 3 for i in x], "g^")

plt.ylabel("Y - axis")
plt.xlabel("X - axis")
plt.show()
