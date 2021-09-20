import matplotlib.pyplot as plt

x = [x * 0.1 for x in range(0, 10)]

plt.plot(x, x, "r--", label="linear")
plt.plot(x, [i ** 2 for i in x], "bs", label="quadratic")
plt.plot(x, [i ** 3 for i in x], "g^", label="cubic")


plt.ylabel("Y - axis")
plt.xlabel("X - axis")

plt.legend()

plt.show()
