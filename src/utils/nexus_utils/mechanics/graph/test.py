
import numpy as np

"""
Creating and Manipulating Arrays
"""
A = np.array([1, 2, 3])  # 1D array
B = np.array([[1, 2], [3, 4]])  # 2D matrix
C = np.linspace(0, 10, 5)  # 5 values between 0 and 10
D = np.arange(0, 10, 2)  # Values from 0 to 10, step 2

print("Array A:", A)
print("Matrix B:\n", B)
print("Linspace C:", C)
print("Arange D:", D)

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

"""
Basic operations
"""

sum_xy = x + y  # Element-wise addition
prod_xy = x * y  # Element-wise multiplication
sqrt_x = np.sqrt(x)  # Square root

print("Sum:", sum_xy)
print("Product:", prod_xy)
print("Square Root:", sqrt_x)


"""
Plotting a Basic Function
"""

import matplotlib.pyplot as plt

# Function: F(t) = ma - mg over time
t = np.linspace(0, 5, 100)  # Time from 0 to 5 seconds
m, a, g = 2, 10, 9.81
F = m * a - m * g  # Net Force

plt.plot(t, np.full_like(t, F), label=r'$F(t) = ma - mg$', color='blue', linewidth=2)

plt.xlabel("Time (s)")
plt.ylabel("Force (N)")
plt.title("Net Force Over Time")
plt.legend()
plt.grid(True)
plt.show()

"""
Multiple Graphs & Customization
"""
t = np.linspace(0, 10, 100)
y1 = np.sin(t)
y2 = np.cos(t)

plt.figure(figsize=(8, 5))
plt.plot(t, y1, label="Sine Wave", color="red")
plt.plot(t, y2, label="Cosine Wave", color="blue", linestyle="--")

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sine & Cosine Waves")
plt.legend()
plt.grid()
plt.show()

"""
3D Graphs for Nexus Simulations
"""
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = t  # Represents time

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label="3D Nexus Curve")

ax.set_xlabel("X (sin)")
ax.set_ylabel("Y (cos)")
ax.set_zlabel("Z (time)")
ax.set_title("3D Motion in Nexus Theory")
ax.legend()
plt.show()


