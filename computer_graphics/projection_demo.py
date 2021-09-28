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
                                             alpha=0.25))

def build_projection_matrix(camera, dist=1):
    """
    Builds a simple projection matrix given a camera position
    and the distance of the viewing plane from the camera.
    """
    proj = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1/dist, 0]])

    return proj


def draw_camera(ax, camera_pos, view_plane, view_faces):
    draw(ax, camera_pos)
    draw(ax, view_plane, view_faces)
    for i in range(len(view_plane)):
        ax.plot([camera_pos[0, 0], view_plane[i, 0]],
                [camera_pos[0, 1], view_plane[i, 1]],
                [camera_pos[0, 2], view_plane[i, 2]], c='k')


def main():
    # Viewing Plane
    view_plane = np.array([[-1, -1, 1],
                           [1, -1, 1],
                           [1, 1, 1],
                           [-1, 1, 1]])

    faces = [[view_plane[0], view_plane[1], view_plane[2], view_plane[3]]]

    # Camera location
    camera = np.array([[0, 0, 0]])

    # Point in 3D space
    point = np.array([[1.5, 1.5, 3]])

    # Get the projection matrix and calculate the projected point.
    proj_matrix = build_projection_matrix(camera)

    proj_point = proj_matrix @ np.append(point, 1)
    proj_point /= proj_point[3]
    proj_point = np.expand_dims(proj_point, axis=0)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-1, 3])

    # Draw camera
    draw_camera(ax, camera, view_plane, faces)
    draw(ax, point)
    draw(ax, proj_point)

    # Draw line from camera to the 3D point
    ax.plot([camera[0, 0], point[0, 0]],
            [camera[0, 1], point[0, 1]],
            [camera[0, 2], point[0, 2]], c='k')

    plt.show()


if __name__ == "__main__":
    main()
