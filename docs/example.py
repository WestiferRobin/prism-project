import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
h_initial = 100.0  # initial height (m)
v_initial = 0.0  # initial velocity (m/s)
dt = 0.01  # time step (s)

# Time array
t = np.arange(0, np.sqrt(2 * h_initial / g) + dt, dt)  # total time array based on freefall time

# Kinematic equations for freefall
height = h_initial - 0.5 * g * t**2  # height as a function of time
velocity = v_initial - g * t        # velocity as a function of time

# Adjust height to zero out after hitting the ground
height = np.maximum(height, 0)

# Plotting
plt.figure(figsize=(10, 6))

# Height vs. Time
plt.subplot(2, 1, 1)
plt.plot(t, height, label="Height (m)", color="blue")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Freefall: Height vs. Time")
plt.legend()
plt.grid()

# Velocity vs. Time
plt.subplot(2, 1, 2)
plt.plot(t, velocity, label="Velocity (m/s)", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Freefall: Velocity vs. Time")
plt.legend()
plt.grid()

# Display plots
plt.tight_layout()
plt.show()
