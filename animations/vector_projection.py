from manim import *

class VectorProjection(ThreeDScene):
    def construct(self):
        # Setup the axes and the plane
        axes = ThreeDAxes()
        plane = NumberPlane()

        # Setup the vectors
        vector = Arrow3D([0, 0, 0], [2, 3, 2], color=YELLOW).set_shade_in_3d(True)
        # projection = Arrow3D([0, 0, 0], [2, 3, 0], color=GREEN)
        # projection_line = DashedLine([2, 3, 0], [2, 3, 2], color=WHITE)

        # Create labels
        # vector_label = MathTex("\\vec{a}").next_to(vector.get_end(), RIGHT)
        # proj_label = MathTex("\\text{proj}").next_to(projection.get_end(), RIGHT)

        # Add objects to the scene
        self.add(axes, plane, vector)
        # self.add(plane, axes, vector, projection, projection_line)
        # self.play(Create(vector))
        # self.wait(1)
        # self.play(Create(projection), Create(projection_line))
        # self.wait(1)

        # Add labels
        # self.add_fixed_in_frame_mobjects(vector_label)  # Labels stay while scene is rotating
        # self.add_fixed_in_frame_mobjects(proj_label)

        # Rotate and show the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=0.2)
        # self.wait(5)
        # self.stop_ambient_camera_rotation()
