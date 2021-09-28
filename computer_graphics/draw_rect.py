import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def draw(ax, verts, faces=[]):
    """
    Draw the object defined by vertices and faces.
    """

    ax.scatter3D(verts[:, 0], verts[:, 1], verts[:, 2])

    if faces:
        ax.add_collection3d(Poly3DCollection(faces,
                                             facecolors='blue',
                                             linewidths=1,
                                             edgecolor='b',
                                             alpha=0.5))


def main():
    points = np.array([[-1, -1, 0],
                       [1, -1, 0],
                       [1, 1, 0],
                       [-1, 1, 0]])

    # Transformation Matrix
    transform = np.eye(3) * 1.0
    points = points @ transform

    faces = [[points[0], points[1], points[2], points[3]]]


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    draw(ax, points, faces)

    plt.show()


if __name__ == "__main__":
    main()
