from manim import *

class AreaUnderCurve(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4,4,1],
            y_range=[-3,3,1]
        ).scale(1.5)
        curve = axes.plot(lambda x: np.exp(-(x-1)**2), color=BLUE, stroke_width=0.5)
        area = axes.get_riemann_rectangles(graph=curve, x_range=[-4, 4], color=GREEN, dx=0.1).set_stroke(width=0.1, color=GREEN)
        self.play(Create(axes), run_time=2)
        self.play(Create(curve), run_time=2)
        self.play(FadeIn(area), run_time=2)
        self.wait(2)
        for dx in [0.1, 0.09, 0.05,0.03, 0.02, 0.01, 0.009, 0.005, 0.003, 0.002, 0.001]:
            new_area = axes.get_riemann_rectangles(graph=curve, x_range=[-4, 4], color=GREEN, dx=dx).set_stroke(width=dx, color=GREEN)
            self.play(Transform(area, new_area), run_time=2)
            self.wait(5)