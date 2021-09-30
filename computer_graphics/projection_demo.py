import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def draw(ax, verts, faces=[]):
    """
    Draw the object defined by vertices and faces.
    """

    if verts.ndim == 1:
        ax.scatter3D(verts[0], verts[1], verts[2])
    else:
        ax.scatter3D(verts[:, 0], verts[:, 1], verts[:, 2])

    if faces:
        ax.add_collection3d(Poly3DCollection(faces,
                                             facecolors='blue',
                                             linewidths=1,
                                             edgecolor='b',
                                             alpha=0.25))

def build_projection_matrix(near=1):
    """
    Builds a simple projection matrix given the distance of the viewing plane
    from the camera.
    """
    proj = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1/near, 0]])

    return proj


def draw_camera(ax, camera_pos, view_plane, view_faces):
    draw(ax, camera_pos)
    draw(ax, view_plane, view_faces)
    for i in range(len(view_plane)):
        ax.plot([camera_pos[0], view_plane[i, 0]],
                [camera_pos[1], view_plane[i, 1]],
                [camera_pos[2], view_plane[i, 2]], c='k')


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def look_at(src, to):
    """Creates a camera matrix located at `src` looking towards `to`."""
    forward = normalize(src - to)
    right = np.cross(np.array([0, 1, 0]), forward)
    up = np.cross(forward, right)

    camera_matrix = np.eye(4)
    camera_matrix[:3, 0] = right
    camera_matrix[:3, 1] = up
    camera_matrix[:3, 2] = forward
    camera_matrix[:3, 3] = src

    return camera_matrix


def transform_point(point, T):
    proj_point = T @ np.append(point, 1)
    proj_point /= proj_point[3]

    return proj_point[:3]


def main():
    # Camera location
    camera = np.array([0.5, 0.5, 0.5])

    # Build camera matrix
    camera_matrix = look_at(camera, np.array([0, 0, -1]))

    # Viewing Plane
    view_plane = np.array([[-1, -1, 1],
                           [1, -1, 1],
                           [1, 1, 1],
                           [-1, 1, 1]])

    # Transform viewing plane to match camera
    view_plane = camera_matrix @ np.vstack((view_plane.T, np.ones(4)))
    view_plane = view_plane[:3].T

    faces = [[view_plane[0], view_plane[1], view_plane[2], view_plane[3]]]

    # Point in 3D space
    point = np.array([[1.5, 1.5, 3]])

    # Get the projection matrix and calculate the projected point.
    proj_matrix = build_projection_matrix()

    fig = plt.figure()
    ax3d = fig.add_subplot(121, projection='3d')
    ax2d = fig.add_subplot(122)
    ax3d.set_xlim([-2, 2])
    ax3d.set_ylim([-2, 2])
    ax3d.set_zlim([-1, 3])

    point -= camera
    proj_point = transform_point(point, proj_matrix)
    proj_point += camera
    point += camera

    # Transform to camera space
    T = np.linalg.inv(camera_matrix) @ proj_matrix
    camera_point = transform_point(point, T)

    # Draw camera
    draw_camera(ax3d, camera, view_plane, faces)
    draw(ax3d, point)
    draw(ax3d, proj_point)

    # Draw line from camera to the 3D point
    ax3d.plot([camera[0], point[0, 0]],
              [camera[1], point[0, 1]],
              [camera[2], point[0, 2]], c='k')

    print(camera_point)
    ax2d.scatter(camera_point[0], camera_point[1])
    ax2d.set_xlim([-1, 1])
    ax2d.set_ylim([-1, 1])

    plt.show()


if __name__ == "__main__":
    main()
