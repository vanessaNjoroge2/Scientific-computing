import numpy as np

# Set up a grid
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
dx = dy = 1/100

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Approximate volume using Riemann sum
volume = np.sum(Z) * dx * dy
print("Estimated volume under the surface z = x² + y²:", volume)
