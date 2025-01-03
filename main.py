import matplotlib.pyplot as plt
import numpy as np

"""
Orb problem

0 <= t <= 2: Launch to Ready Position
- ma = F_thrust - mg => F_thrust = ma + mg = m(a + g)
- v(0) = 0 m/s = ds(0)/dt
- s(0) = 0 and s(2) = 5 m

2 < t <= 4: Hover
- 0 = F_thrust + F_impulse - mg => m*a_thrust + m*a_impulse - m*g = 0 => a_impulse = g - a_thrust
- v(2) = v(2) from Launch
- s(2) = s(4) = 5 m

"""

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
a_thrust = 2.50  # Thrust acceleration (m/s^2)
c = 3e8  # Speed of light (m/s)

# Initial conditions
time_launch = np.linspace(0, 2, 100)  # Time array for launch phase
time_hover = np.linspace(2, 4, 100)   # Time array for hover phase

# Functions to calculate velocity and position
def velocity(a, t, v_0=0):
    return v_0 + (a * t)

def position(a, t, v_0=0, s_0=0):
    return s_0 + (v_0 * t) + (0.5 * a * (t ** 2))

# Launch phase: From t=0 to t=2
v_launch = velocity(a_thrust + g, time_launch)
s_launch = position(a_thrust + g, time_launch)

# Hover phase: From t=2 to t=4
a_impulse = g - a_thrust  # Impulse acceleration during hover
v_hover = velocity(a_impulse, time_hover, v_launch[-1])
s_hover = position(a_impulse, time_hover, v_launch[-1], s_launch[-1])

# Plotting
plt.figure(figsize=(10, 6))

# Height vs. Time
plt.subplot(2, 1, 1)
plt.plot(time_launch, s_launch, label="Height (m) - Launch", color="blue")
plt.plot(time_hover, s_hover, label="Height (m) - Hover", color="green")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Height vs. Time")
plt.legend()
plt.grid()

# Velocity vs. Time
plt.subplot(2, 1, 2)
plt.plot(time_launch, v_launch, label="Velocity (m/s) - Launch", color="blue")
plt.plot(time_hover, v_hover, label="Velocity (m/s) - Hover", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs. Time")
plt.legend()
plt.grid()

# Display plots
plt.tight_layout()
plt.show()
