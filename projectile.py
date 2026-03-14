from manim import *

class ProjectileMotion(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-1, 10, 1),
            y_range=(-1, 5, 1),
            z_range=(-1, 1, 1),
            x_length=12,
            y_length=7,
            z_length=3,
            x_axis_config={"include_ticks": False, "include_numbers": False},
            y_axis_config={"include_ticks": False, "include_numbers": False},
            z_axis_config={"stroke_opacity":0},
            tips=False
        )
        self.play(Create(axes), run_time=2)
        self.wait(1)
        # Physics parameters
        v0 = 10
        angle = 45 * DEGREES
        g = 9.8

        def parabolic_func():
            return ParametricFunction(
                lambda t: axes.c2p(
                    v0 * np.cos(angle) * t,
                    v0 * np.sin(angle) * t - 0.5 * g * t**2,
                    0
                ),
                t_range=(0, 10)
            ).set_stroke(width=2)
        
        parabola = parabolic_func()
        self.play(Create(parabola), run_time=2)
        