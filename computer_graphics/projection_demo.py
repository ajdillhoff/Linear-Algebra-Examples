import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def draw(ax, verts, faces=[], color=[]):
    """
    Draw the object defined by vertices and faces.
    """

    if verts.ndim == 1:
        if color:
            ax.scatter3D(verts[0], verts[1], verts[2], c=color)
        else:
            ax.scatter3D(verts[0], verts[1], verts[2], c=color)
    else:
        if color:
            ax.scatter3D(verts[:, 0], verts[:, 1], verts[:, 2], c=color)
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


def look_at(src, to, up):
    """Creates a camera matrix located at `src` looking towards `to`."""
    forward = normalize(src - to)
    right = np.cross(normalize(up), forward)
    up = np.cross(forward, right)

    forward = -forward

    camera_matrix = np.array([
        [right[0], right[1], right[2], -np.dot(right, src)],
        [up[0], up[1], up[2], -np.dot(up, src)],
        [forward[0], forward[1], forward[2], -np.dot(forward, src)],
        [0, 0, 0, 1]
    ])

    return camera_matrix


def transform_point(point, T):
    proj_point = T @ np.append(point, 1)
    proj_point /= proj_point[3]

    return proj_point[:3]


def transform_points(points, T):
    homogeneous_points = np.hstack((points, np.ones((len(points), 1))))
    proj_points = T @ homogeneous_points.T
    proj_points /= proj_points[3, :]

    return proj_points[:3, :].T


def main():
    # Camera location
    camera = np.array([0.2, 0.5, 0.0])
    at = np.array([1.0, 0.0, 0.0])
    up = np.array([0.0, 0.0, 1.0])

    # Build camera matrix
    camera_matrix = look_at(camera, at, up)

    # Viewing Plane
    view_plane = np.array([[-1, -1, 1],
                           [1, -1, 1],
                           [1, 1, 1],
                           [-1, 1, 1]])

    # Transform viewing plane to match camera
    view_plane = transform_points(view_plane, np.linalg.inv(camera_matrix))

    faces = [[view_plane[0], view_plane[1], view_plane[2], view_plane[3]]]

    # Points in 3D space
    points = np.array([[4, 0., 1],
                       [3, 0, 0],
                       [4, -1, 0],
                       [5, 0, 0],
                       [4, 1, 0]])

    # Get the projection matrix and calculate the projected point.
    proj_matrix = build_projection_matrix()

    fig1 = plt.figure()
    fig2 = plt.figure()
    ax3d = fig1.add_subplot(111, projection='3d')
    ax2d = fig2.add_subplot(111)
    ax3d.set_xlim([0, 4])
    ax3d.set_ylim([-2, 2])
    ax3d.set_zlim([-2, 2])
    ax3d.set_xlabel("X")
    ax3d.set_ylabel("Y")
    ax3d.set_zlabel("Z")

    proj_point = transform_points(points, np.linalg.inv(camera_matrix) @ proj_matrix @ camera_matrix)

    # Transform to camera space
    T = proj_matrix @ camera_matrix
    camera_points = transform_points(points, T)

    # Draw camera
    draw_camera(ax3d, camera, view_plane, faces)
    draw(ax3d, points)
    draw(ax3d, proj_point)

    # Draw line from camera to the 3D point
    for i in range(points.shape[0]):
        ax3d.plot([camera[0], points[i, 0]],
                  [camera[1], points[i, 1]],
                  [camera[2], points[i, 2]], c='r')

    ax2d.scatter(camera_points[:, 0], camera_points[:, 1], c=points[:, 2])
    ax2d.set_xlim([-1, 1])
    ax2d.set_ylim([-1, 1])

    plt.show()


if __name__ == "__main__":
    main()
