import matplotlib.pyplot as plt
import numpy as np

# Define origin points
origin = np.array([[0, 0], [0, 0]])  # two vectors starting at (0,0)

# Define vector components
vectors = np.array([[2, 1], [1, 3]])  # (x,y) components of each vector

# Plot vectors using quiver
plt.quiver(*origin.T, vectors[:,0], vectors[:,1], 
           angles='xy', scale_units='xy', scale=1, color=['r','b'])

# Set axis limits
plt.xlim(-1, 4)
plt.ylim(-1, 4)

# Add grid and labels
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Vector Diagram using Matplotlib')

plt.show()
