from manim import *
import math

class DynamicElectricField(Scene):
    def construct(self):
        axes = Axes(
            x_axis_config={"stroke_opacity": 0},
            y_axis_config={"stroke_opacity": 0},
            tips=False
        )

        charge = MathTex("Q+").set_color(YELLOW)
        self.add(axes, charge)
        self.wait(2)
        path = axes.plot(lambda x: x - (x ** 3) / math.factorial(3) + (x ** 5) / math.factorial(5), x_range=(-4, 4))

        def electric_field():
            vectors = VGroup()
            
            for x in np.linspace(-10, 10, 26):
                for y in np.linspace(-5, 5, 16):
                    position = axes.c2p(x, y)
                    r_vector = position - charge.get_center()
                    disp = np.linalg.norm(r_vector)
                    if disp < 0.4:
                        continue

                    r_hat = r_vector / disp

                    E = 1 / (disp ** 2)
                    E = np.clip(E, 0, 0.4)

                    vector = Vector(
                        r_hat * E,
                        color = interpolate_color(YELLOW, ORANGE, E / 0.4),
                        tip_length = 0.15,
                        max_tip_length_to_length_ratio = 0.5
                    )
                    vector.move_to(position)
                    vectors.add(vector)

            return vectors
        
        dynamic_field = always_redraw(electric_field)
        self.add(dynamic_field)

        self.play(
            MoveAlongPath(
                charge,
                path=path
            ),
            run_time=10,
            rate_func=linear
        )
        self.wait(2)