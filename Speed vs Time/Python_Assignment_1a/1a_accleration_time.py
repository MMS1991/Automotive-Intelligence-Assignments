import matplotlib.pyplot as plt
import numpy as np

# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20.5]

# Speed (km/h)
speed = [0, 40, 42, 37, 36, 31, 8, 32, 8, 26, 11, 0, 5, 15, 29, 42, 46, 37, 40, 25, 4, 0]

# Calculate acceleration (km/h per minute)
acceleration = np.diff(speed)  # delta speed
time_acc = time[1:]            # corresponding time values

plt.figure()
plt.plot(time_acc, acceleration, marker='o')
plt.xlabel("Time (minutes)")
plt.ylabel("Acceleration (km/h per minute)")
plt.title("Acceleration vs Time")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20.5]
speed = [0, 40, 42, 37, 36, 31, 8, 32, 8, 26, 11, 0, 5, 15, 29, 42, 46, 37, 40, 25, 4, 0]

# 1. Calculate the area using the Trapezoidal Rule
# We divide by 60 to convert the time from minutes to hours
total_distance_km = np.trapz(speed, time) / 60

# 2. Create the Plot
plt.plot(time, speed, marker='o', color='blue', label='Speed (km/h)')

# 3. Fill the area under the curve to represent distance
plt.fill_between(time, speed, color='skyblue', alpha=0.4, label='Distance (Area)')

# Formatting the chart
plt.xlabel("Time (minutes)")
plt.ylabel("Speed (km/h)")
plt.title(f"Speed vs Time\nTotal Distance Traveled: {total_distance_km:.2f} km")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.savefig('speed_time_distance.png')