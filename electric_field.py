from manim import *
import math

class ElectricField(Scene):
    def construct(self):
        axes = Axes(
            x_axis_config={"stroke_opacity": 0},
            y_axis_config={"stroke_opacity": 0},
            tips=False
        )
        self.play(Create(axes), run_time=1)
        self.wait(1)
        charge = MathTex("Q+").set_color(color=YELLOW).move_to(axes.c2p(0, 0)).scale(0.8)
        self.play(Write(charge), run_time=3)
        vector_data = []
        for x in np.linspace(-8, 8, 40):
            for y in np.linspace(-6, 6, 28):
                r = np.array([x, y, 0])
                d = np.hypot(x, y)
                if d < 0.33:
                    continue

                direction = r / d

                E = 1 / (d**2)
                E = np.clip(E, 0, 0.4)

                vector = Vector(
                    direction * E,
                    color=interpolate_color(ORANGE, YELLOW, E / 0.4)
                )
                vector.shift(r)
                vector_data.append((d, vector))

        vector_data.sort(key=lambda item: item[0])
        vectors = VGroup(*[v for _, v in vector_data])

        self.play(
            LaggedStart(
                *[GrowArrow(v) for v in vectors],
                lag_ratio=0.03
            ),
            run_time=5
        )
        self.wait(2)

