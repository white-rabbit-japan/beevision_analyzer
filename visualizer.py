import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the pyramid dimensions
pyramid_182 = {
    'top_x': 35,
    'base_x': 100,
    'top_y': 25,
    'base_y': 80,
    'min_size': 5,
    'area_height': 105
}

# Box dimensions
# box = (35, 25, 105)
box = (35, 25, 107)


# Function to create the vertices of the pyramid
def create_pyramid_vertices(pyramid):
    half_base_x = pyramid['base_x'] / 2
    half_base_y = pyramid['base_y'] / 2
    half_top_x = pyramid['top_x'] / 2
    half_top_y = pyramid['top_y'] / 2

    # Vertices of the base rectangle
    base_vertices = np.array([
        [-half_base_x, -half_base_y, 0],
        [half_base_x, -half_base_y, 0],
        [half_base_x, half_base_y, 0],
        [-half_base_x, half_base_y, 0]
    ])

    # Vertices of the top rectangle
    top_vertices = np.array([
        [-half_top_x, -half_top_y, pyramid['area_height']],
        [half_top_x, -half_top_y, pyramid['area_height']],
        [half_top_x, half_top_y, pyramid['area_height']],
        [-half_top_x, half_top_y, pyramid['area_height']]
    ])

    # Combine base and top vertices
    vertices = np.concatenate((base_vertices, top_vertices), axis=0)
    return vertices

# Function to create the vertices of the box


def create_box_vertices(box):
    x, y, z = box
    half_x = x / 2
    half_y = y / 2

    # Vertices of the box
    vertices = np.array([
        [-half_x, -half_y, 0],
        [half_x, -half_y, 0],
        [half_x, half_y, 0],
        [-half_x, half_y, 0],
        [-half_x, -half_y, z],
        [half_x, -half_y, z],
        [half_x, half_y, z],
        [-half_x, half_y, z]
    ])
    return vertices

# Function to plot the pyramid and the box


def plot_pyramid_and_box(pyramid, box):
    pyramid_vertices = create_pyramid_vertices(pyramid)
    box_vertices = create_box_vertices(box)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the faces of the pyramid
    pyramid_faces = [
        [pyramid_vertices[0], pyramid_vertices[1],
            pyramid_vertices[5], pyramid_vertices[4]],
        [pyramid_vertices[1], pyramid_vertices[2],
            pyramid_vertices[6], pyramid_vertices[5]],
        [pyramid_vertices[2], pyramid_vertices[3],
            pyramid_vertices[7], pyramid_vertices[6]],
        [pyramid_vertices[3], pyramid_vertices[0],
            pyramid_vertices[4], pyramid_vertices[7]],
        [pyramid_vertices[4], pyramid_vertices[5],
            pyramid_vertices[6], pyramid_vertices[7]],
        [pyramid_vertices[0], pyramid_vertices[1],
            pyramid_vertices[2], pyramid_vertices[3]]
    ]

    # Define the faces of the box
    box_faces = [
        [box_vertices[0], box_vertices[1], box_vertices[5], box_vertices[4]],
        [box_vertices[1], box_vertices[2], box_vertices[6], box_vertices[5]],
        [box_vertices[2], box_vertices[3], box_vertices[7], box_vertices[6]],
        [box_vertices[3], box_vertices[0], box_vertices[4], box_vertices[7]],
        [box_vertices[4], box_vertices[5], box_vertices[6], box_vertices[7]],
        [box_vertices[0], box_vertices[1], box_vertices[2], box_vertices[3]]
    ]

    # Create 3D polygon collections
    pyramid_poly3d = Poly3DCollection(
        pyramid_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.25)
    box_poly3d = Poly3DCollection(
        box_faces, facecolors='magenta', linewidths=1, edgecolors='b', alpha=0.25)

    ax.add_collection3d(pyramid_poly3d)
    ax.add_collection3d(box_poly3d)

    # Calculate dynamic ticks for x and y axes
    x_ticks = np.linspace(-pyramid['base_x'] / 2, pyramid['base_x'] / 2, num=5)
    y_ticks = np.linspace(-pyramid['base_y'] / 2, pyramid['base_y'] / 2, num=5)
    x_labels = np.linspace(0, pyramid['base_x'], num=5, dtype=int)
    y_labels = np.linspace(0, pyramid['base_y'], num=5, dtype=int)

    # Set the limits, ticks, and labels
    ax.set_xlim([-pyramid['base_x']/2, pyramid['base_x']/2])
    ax.set_ylim([-pyramid['base_y']/2, pyramid['base_y']/2])
    ax.set_zlim([0, max(pyramid['area_height'], box[2])])
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')

    plt.show()


# Plot the pyramid and the box
plot_pyramid_and_box(pyramid_182, box)