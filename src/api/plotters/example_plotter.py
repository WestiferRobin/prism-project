import numpy as np
import matplotlib.pyplot as plt

# Define the line equation (works with scalars or np arrays)
def y(x, slope=1, basis=0):
    return slope * x + basis

# Create x values from -10 to 10 (100 points)
x_vals = np.linspace(-10, 10)

# Get corresponding y values
y_vals = y(x_vals, slope=2, basis=5)

# Plot
plt.plot(x_vals, y_vals, label="y = 2x + 5")
plt.title("Line: y = slope * x + basis")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
