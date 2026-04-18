import matplotlib.pyplot as plt
import numpy as np

# Time in minutes
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20.5]

# Speed in km/h
speed = [0, 40, 42, 37, 36, 31, 8, 32, 8, 26, 11, 0, 5, 15, 29, 42, 46, 37, 40, 25, 4, 0]

# Acceleration calculation
acceleration = np.diff(speed)
time_acc = time[1:]

plt.figure()
plt.plot(time_acc, acceleration, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Acceleration (km/h per minute)")
plt.title("Acceleration vs Time")
plt.grid(True)
plt.show()
