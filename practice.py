from manim import *

class Oscillation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-2, 2, 1),
            y_range=(-1, 1, 1),
            z_range=(-1, 1, 1),
            x_length=3,
            y_length=2,
            z_length=2,
            x_axis_config={"include_ticks": False, "include_numbers": False},
            y_axis_config={"stroke_opacity": 0},
            z_axis_config={"stroke_opacity": 0},
            tips=False
        ).shift(UL * 3.5 + LEFT * 2)
        self.play(Create(axes), run_time=2)
        # Values for the spring system
        N = 20
        R = 0.3
        A = 2.5
        k = 0.3
        w = 2 * PI
        l = 4

        time_tracker = ValueTracker(0)
        def current_length():
            t = time_tracker.get_value()
            return l + A * np.exp(-k * t) * np.sin(w * t)
        def spring_func():
        
            L = current_length()
            return ParametricFunction(
                lambda t: axes.c2p(
                    R * (np.sin(2 * N * w * t / L)),
                    -(0.05 + t),
                    R * (np.cos(2 * N * w * t / L))
                ),
                t_range=(0, L)
            ).set_stroke(width=2, color=GRAY)
        
        spring = always_redraw(lambda: spring_func())
        block = always_redraw(lambda: Square(side_length=1.2).move_to(axes.c2p(0, -(current_length() + 0.6), 0)).set_stroke(color=YELLOW_A).set_fill(color=YELLOW_A, opacity=1))
        displacement_text = always_redraw(lambda: MathTex(
            r"\Delta l = {:+.2f}".format(current_length() - l)
        ).shift(LEFT * 3.5).scale(0.8))
        axes2 = Axes(
            x_range=(-1, 20, 1),
            y_range=(-3, 3, 1),
            x_length=22,
            y_length=6
        ).scale(0.5).to_corner(UR + RIGHT * 4)
        def damping_graph_func():
            return axes2.plot(
                lambda t: A * np.exp(-k * t) * np.sin(w * t),
                x_range=(0, time_tracker.get_value())
            ).set_stroke(width=2, color=YELLOW_A)
        damping_graph = always_redraw(lambda: damping_graph_func())
        self.play(Create(spring), run_time=4)
        self.wait(1)
        self.play(Create(VGroup(block, axes2, damping_graph)), run_time=5)
        self.wait(1)
        self.play(Write(displacement_text), run_time=4)
        self.wait(1)
        self.play(time_tracker.animate.set_value(20), rate_func=linear, run_time=20)