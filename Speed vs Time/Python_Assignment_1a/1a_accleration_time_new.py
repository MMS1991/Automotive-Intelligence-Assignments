import matplotlib.pyplot as plt
import numpy as np

# 1. Define the Data
# Time (minutes)
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20.5]
# Speed (km/h)
speed = [0, 40, 42, 37, 36, 31, 8, 32, 8, 26, 11, 0, 5, 15, 29, 42, 46, 37, 40, 25, 4, 0]

# 2. Calculate Acceleration (km/h per minute)
acceleration = np.diff(speed) 
time_acc = time[1:]

# 3. Calculate Total Distance (km)
# np.trapezoid is the new replacement for np.trapz in NumPy 2.0+
# We divide by 60 because speed is in km/h and time is in minutes
total_distance_km = np.trapezoid(speed, time) / 60

print(f"Total distance traveled: {total_distance_km:.2f} km")

# 4. Visualization
plt.figure(figsize=(12, 5))

# Plot 1: Acceleration
plt.subplot(1, 2, 1)
plt.plot(time_acc, acceleration, marker='o', color='orange')
plt.xlabel("Time (minutes)")
plt.ylabel("Acceleration (km/h per minute)")
plt.title("Acceleration vs Time")
plt.grid(True)

# Plot 2: Speed and Distance Area
plt.subplot(1, 2, 2)
plt.plot(time, speed, marker='o', color='blue', label='Speed')
plt.fill_between(time, speed, color='skyblue', alpha=0.4, label='Distance (Area)')
plt.xlabel("Time (minutes)")
plt.ylabel("Speed (km/h)")
plt.title(f"Speed vs Time\nDistance: {total_distance_km:.2f} km")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()