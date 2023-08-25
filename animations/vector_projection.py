from manim import *

class VectorProjection(ThreeDScene):
    def construct(self):
        # Setup the axes and the plane
        # axes = ThreeDAxes()

        # Create a simple plane using Surface
        plane = Surface(
            lambda u, v: np.array([
                u,
                v,
                0
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(20, 20),
            checkerboard_colors=[BLUE_D, BLUE_D],
            stroke_color=BLUE_D,
            fill_opacity=0.5,
        )

        # Setup the vectors
        vector = Arrow3D([0, 0, 0], [2, 3, 2], color=YELLOW)
        projection = Arrow3D([0, 0, 0], [2, 3, 0.1], color=GREEN)
        projection_line = DashedLine([2, 3, 0.1], [2, 3, 2], color=WHITE)
        distance_line = Arrow3D([0, 0, 0], [0, 0, 2], color=RED)

        # Rotate and show the scene
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # Create labels
        vector_label = MathTex("\\mathbf{b}").next_to(vector.get_end() + .2, RIGHT)
        proj_label = MathTex("\\hat{\mathbf{b}} = \\text{proj}_{\\text{Col} A} \\mathbf{b}").next_to(projection.get_end() + .2, RIGHT)
        distance_label = MathTex("\\mathbf{b} - A\\mathbf{x}").next_to(distance_line.get_end() + .2, RIGHT)

        # Rotate labels to face camera
        # vector_label.rotate(15, RIGHT)
        vector_label.rotate(65 * DEGREES, RIGHT)
        vector_label.rotate(45 * DEGREES, OUT)
        proj_label.rotate(65 * DEGREES, RIGHT)
        proj_label.rotate(45 * DEGREES, OUT)
        distance_label.rotate(65 * DEGREES, RIGHT)
        distance_label.rotate(45 * DEGREES, OUT)

        # Add objects to the scene
        self.add(plane, vector, projection, projection_line, distance_line)

        # Add labels
        # self.add_fixed_in_frame_mobjects(vector_label)  # Labels stay while scene is rotating
        # self.add_fixed_in_frame_mobjects(proj_label)
        self.add(vector_label, proj_label, distance_label)
