from manim import *

class GraphAngle(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80*DEGREES, theta=60*DEGREES)
        axes =  ThreeDAxes(x_range=(-10, 10, 1), y_range=(-3, 3, 1), z_range=(-3, 3, 1), x_length=21, y_length=7, z_length=7)
        self.add(axes)
        self.move_camera(phi=50*DEGREES, theta=180*DEGREES, run_time=10)
        self.wait(2)