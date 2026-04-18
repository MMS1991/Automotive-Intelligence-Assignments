import matplotlib.pyplot as plt

# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20.5]

# Speed (km/h)
speed = [0, 40, 42, 37, 36, 31, 8, 32, 8, 26, 11, 0, 5, 15, 29, 42, 46, 37, 40, 25, 4, 0]


distance_2min = []
plot_time = []

for i in range(len(speed) - 1):
    avg_speed = (speed[i] + speed[i + 1]) / 2
    distance = avg_speed * (2 / 60)   # distance in km (2 minutes)
    distance_2min.append(distance)
    plot_time.append(time[i + 1])     # midpoint time

plt.figure()
plt.plot(plot_time, distance_2min, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Distance covered in 2 minutes (km)")
plt.title("Distance Covered Every 2 Minutes")
plt.grid(True)
plt.show()
