import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def draw_box(ax, origin, size, color='white', edge='black', alpha=1.0):
    x, y, z = origin
    dx, dy, dz = size

    # Define the 8 vertices of the box
    vertices = np.array([
        [x, y, z],
        [x+dx, y, z],
        [x+dx, y+dy, z],
        [x, y+dy, z],
        [x, y, z+dz],
        [x+dx, y, z+dz],
        [x+dx, y+dy, z+dz],
        [x, y+dy, z+dz]
    ])

    # Define the 6 faces using the vertices
    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],
        [vertices[j] for j in [4, 5, 6, 7]],
        [vertices[j] for j in [0, 1, 5, 4]],
        [vertices[j] for j in [2, 3, 7, 6]],
        [vertices[j] for j in [1, 2, 6, 5]],
        [vertices[j] for j in [3, 0, 4, 7]]
    ]

    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, edgecolors=edge, alpha=alpha))

# Set up figure and axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Main house base (2 floors)
draw_box(ax, (0, 0, 0), (10, 6, 3), color='white')        # Ground floor
draw_box(ax, (0, 0, 3), (10, 6, 3), color='white')        # First floor

# Roof slab
draw_box(ax, (0, 0, 6), (10, 6, 0.3), color='lightgray')

# Balcony front extension with railing
draw_box(ax, (0, 6, 3.8), (10, 0.3, 0.8), color='gray')   # balcony wall
draw_box(ax, (0.5, 6.3, 3.8), (2, 0.2, 0.8), color='black')  # deco panel left
draw_box(ax, (7.5, 6.3, 3.8), (2, 0.2, 0.8), color='black')  # deco panel right

# Side extension block
draw_box(ax, (10, 4, 0), (2, 2, 3), color='white')
draw_box(ax, (10, 4, 3), (2, 2, 2), color='white')

# Windows and doors (simplified)
draw_box(ax, (1, 0, 1), (2, 0.1, 1.5), color='skyblue')   # Ground floor window
draw_box(ax, (4, 0, 0), (2, 0.1, 2.5), color='saddlebrown')  # Door
draw_box(ax, (1, 0, 4), (2, 0.1, 1.2), color='skyblue')   # First floor window

# Steps
draw_box(ax, (4, -1.5, 0), (2, 1.5, 0.5), color='lightgray')
draw_box(ax, (4, -1.2, 0.5), (2, 1.2, 0.5), color='lightgray')
draw_box(ax, (4, -0.9, 1.0), (2, 0.9, 0.5), color='lightgray')

# Set camera view
ax.set_xlim(-2, 15)
ax.set_ylim(-3, 10)
ax.set_zlim(0, 7)
ax.view_init(elev=20, azim=-35)
ax.axis('off')
plt.title("3D Oblique-style Drawing of House")
plt.tight_layout()
plt.show()

