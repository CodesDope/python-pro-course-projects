import matplotlib.pyplot as plt
import numpy as np
import math

angle = float(input("Enter angle (degree): "))
velocity = float(input("Enter Velocity (m/s): "))

g = 9.81

cos_theta = math.cos(math.radians(angle))
sin_theta = math.sin(math.radians(angle))

v_x = velocity * cos_theta
v_y = velocity * sin_theta

time_of_flight = (2 * v_y) / g
range_of_flight = time_of_flight * v_x
max_height = (v_y ** 2) / (2 * g)

time = np.linspace(0, time_of_flight, num=200)

y_coords = [(v_y * t) - (0.5 * g * (t ** 2)) for t in time]

plt.ylabel("height (m)")
plt.xlabel("time (s)")
plt.title("Projectile Trajectory")
plt.text(
    time_of_flight / 2,
    max_height / 2,
    f"Time of Flight: {time_of_flight}s",
    ha="center",
    va="center",
)
plt.text(
    time_of_flight / 2,
    max_height / 3,
    f"Range of Flight: {range_of_flight}m",
    ha="center",
    va="center",
)
plt.text(
    time_of_flight / 2,
    max_height / 4,
    f"Maximum Height: {max_height}m",
    ha="center",
    va="center",
)

plt.plot(time, y_coords)
plt.show()
