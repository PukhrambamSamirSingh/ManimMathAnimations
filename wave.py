from manim import *

class WaveForm(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-4, 8, 1),
            y_range=(-2, 2, 1),
            z_range=(-3, 3, 1),
            x_length=13,
            y_length=5,
            z_length=7
        )
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-45 * DEGREES)
        func = lambda t: np.exp(-0.5 * t**2) * np.cos(3 * t)
        phase = ValueTracker(0)
        graph = ParametricFunction(
                    lambda t: axes.c2p(t, 0, func(t) + 0.5 * np.sin(2 * np.pi * t + phase.get_value())),
                    t_range=(-4, 8),
                    color=YELLOW_E
                ).set_stroke(width=2)
        self.play(Create(graph), run_time=5)
        graph.add_updater(
            lambda g: g.become(
                ParametricFunction(
                    lambda t: axes.c2p(t, 0, func(t) + 0.5 * np.sin(2 * np.pi * t + phase.get_value())),
                    t_range=(-4, 8),
                    color=YELLOW_E
                ).set_stroke(width=2)
            )
        )
        self.move_camera(phi=45 * DEGREES, theta=20 * DEGREES)
        self.play(phase.animate.set_value(2 * np.pi), rate_func=linear, run_time=5)
        self.wait(2)