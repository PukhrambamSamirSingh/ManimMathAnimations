from manim import *

class Flow(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=60*DEGREES)
        axes = ThreeDAxes(
            x_range=(-5, 7, 1),
            y_range=(-5, 5, 1),
            z_range=(-5, 5, 1),
            x_length=13,
            y_length=11,
            z_length=11,
            x_axis_config={"include_ticks": False},
            y_axis_config={"include_ticks": False},
            z_axis_config={"include_ticks": False},
            tips=False
        )
        self.add(axes)
        sphere = Sphere(radius=1, resolution=32)
        sphere.move_to(axes.c2p(0, 0, 0))
        self.play(Create(sphere), run_time=4)
        self.wait(1)
        def fluid_flow(pos):
            cx, cy, cz = -2, 0, 0
            x, y, z = pos - np.array([cx, cy, cz])
            r = np.sqrt(x**2 + y**2 + z**2)
            R = 1
            vx = 1
            vy = 0
            vz = 0
            if r < 3 * R:
                strength = (R**3) / (r**3 + 1e-6)
                vy += strength * (y / r)
                vz += strength * (z / r)

            return np.array([vx, vy, vz])

        stream = StreamLines(
            func=fluid_flow,
            color=YELLOW,
            max_anchors_per_line=50,
            padding=1,
            virtual_time=5,
            stroke_width=1
        )
        self.add(stream)
        stream.start_animation(warm_up=True, flow_speed=1.5)
        self.wait(10)