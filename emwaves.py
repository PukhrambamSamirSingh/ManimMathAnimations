from manim import *

class EMWaves(ThreeDScene):
    def construct(self):
        k = ValueTracker(0)
        self.set_camera_orientation(phi=60*DEGREES, theta=-60*DEGREES)
        axes = ThreeDAxes(x_range=(-10, 10, 1), y_range=(-2, 2, 1), z_range=(-3, 3, 1), x_length=21, y_length=5, z_length=7).scale(0.5)
        self.play(Create(axes), run_time=2)
        self.wait(1)
        func1 = lambda t: np.sin(t)
        r = 1
        circle_yz = always_redraw(
            lambda: Circle(radius=1, color=YELLOW, fill_opacity=0.5, fill_color=GREEN_E)
            .set_stroke(width=1)
            .rotate(90 * DEGREES, axis=UP)   # rotate into YZ plane
            .move_to(axes.c2p(0, 0, 0))
        )
        # graph1 = always_redraw(
        #     lambda: ParametricFunction(
        #         lambda t: axes.c2p(t, func1(t + k.get_value()), 0), t_range=(-10, 10),
        #         ).set_stroke(width=2, color=YELLOW)
        # )
        # graph2 = always_redraw(
        #     lambda: ParametricFunction(
        #         lambda t: axes.c2p(t, 0, func1(t + k.get_value())), t_range=(-10, 10),
        #         ).set_stroke(width=2, color=YELLOW)
        #     )
        sample_points = np.linspace(-10, 10, 50)
        arrows = VGroup()
        for t0 in sample_points:
            # Blue arrow (x → y plane)
            arrow_y = always_redraw(
                lambda t0=t0: Arrow(
                    axes.c2p(t0, 0, 0),
                    axes.c2p(t0, func1(t0 + k.get_value()), 0),
                    buff=0,
                    color=BLUE
                )
            )
            # 🔴 Red arrow (x → z plane)
            arrow_z = always_redraw(
                lambda t0=t0: Arrow(
                    axes.c2p(t0, 0, 0),
                    axes.c2p(t0, 0, func1(t0 + k.get_value())),
                    buff=0,
                    color=RED
                )
            )
            arrows.add(arrow_y, arrow_z)
        graphs = VGroup(circle_yz)
        self.play(Create(graphs), run_time=5)
        self.play(*[GrowArrow(a) for a in arrows], run_time=5)
        self.wait(4)
        self.play(k.animate.set_value(4 * np.pi), run_time=15, rate_func=linear)
        self.wait(2)
