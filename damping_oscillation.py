from manim import *

class DampingOscillation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-2, 2, 1),
            y_range=(-1, 1, 1),
            z_range=(-1, 1, 1),
            x_length=5,
            y_length=2,
            z_length=2,
            x_axis_config={"include_ticks":False, "include_numbers":False},
            y_axis_config={"stroke_opacity":0},
            z_axis_config={"stroke_opacity":0},
            tips=False
        ).shift(UL * 3.5).scale(0.8)
        self.play(Create(axes), run_time=1)
        self.wait(1)

        # Values for the oscillation system
        N = 20
        A = 2.5 # amplitude
        l = 4 # natural length of spring
        k = 0.3 # spring constant
        w = 2 * PI
        R = 0.3

        time_tracker = ValueTracker(0)
        def current_l():
            t = time_tracker.get_value()
            return l + A * np.exp(-k * t) * np.sin(w * t)
        
        def spring_func():
            L = current_l()
            return always_redraw(lambda: ParametricFunction(
                lambda t: axes.c2p(
                    R * (np.sin(2 * PI * N * t / L)),
                    -(0.05 + t),
                    R * (np.cos(2 * PI * N * t / L))
                ),
                t_range=(0, L)
            ).set_stroke(width=2, color=GRAY))
        
        spring = always_redraw(spring_func)
        block = always_redraw(lambda: Square(side_length=1.3).move_to(axes.c2p(0, -(current_l()+0.86), 0)).set_stroke(width=2, color=BLUE).set_fill(color=BLUE_C, opacity=1))
        displacement_text = always_redraw(lambda: MathTex(
            f"\\Delta l = {current_l() - l:.2f}"
        ).next_to(block).scale(0.8))
        axes2 = Axes(
            x_range=(0, 20, 2),
            y_range=(-3, 3, 1),
            x_length=6,
            y_length=3,
            tips=False
        ).to_corner(UR)
        self.play(Create(VGroup(spring, block, axes2)), run_time=4)
        self.play(Write(displacement_text), run_time=2)
        # Damped oscillation function
        damping_graph = always_redraw(
            lambda: axes2.plot(
                lambda x: A * np.exp(-k * x) * np.sin(w * x),
                x_range=[0, time_tracker.get_value()]
            ).set_stroke(width=2, color=YELLOW)
        )
        self.play(Create(damping_graph), run_time=2)
        self.wait(1)
        self.play(time_tracker.animate.set_value(20), rate_func=linear, run_time=20)
        self.wait(5)