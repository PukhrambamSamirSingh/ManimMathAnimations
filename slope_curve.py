from manim import *

class SlopeCurve(Scene):
    def construct(self):
        axes = NumberPlane(x_range=[-8, 8, 1], y_range=[-3, 3, 1], background_line_style={"stroke_opacity": 0.1})
        k = ValueTracker(-3)
        self.add(axes)
        # func = lambda x: np.clip(np.exp(5 * x**2) * np.sin(4 * x), -3, 3)
        func = lambda x: 2*np.exp(-0.5 * x**2) * np.sin(4 * x)
        graph = axes.plot(func, color=BLUE)
        self.play(Create(graph), run_time=3)
        self.wait(2)
        slope = always_redraw(lambda: axes.get_secant_slope_group(x=k.get_value(), graph=graph, dx=0.01, secant_line_length=4).set_stroke(width=2, color=GREEN_A))
        dot = always_redraw(lambda: Dot().move_to(axes.c2p(k.get_value(), func(k.get_value()))))
        self.add(slope, dot)
        self.wait(2)
        self.play(k.animate.set_value(3), run_time=20)
        self.wait(4)