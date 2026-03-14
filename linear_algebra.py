from manim import *

class LinearAlgebra(Scene):
    def construct(self):
        axes = NumberPlane().set_stroke(opacity=0.5)
        self.play(Create(axes), run_time = 5)
        self.wait(1)
        vector_line_a = axes.plot(lambda x: 0.2 * x, x_range=[-8, 8]).set_stroke(width=2)
        vector_a = MathTex(r"\vec{a}").move_to(axes.c2p(6, 1))
        self.play(Create(vector_line_a), run_time = 4)
        self.play(Write(vector_a), run_time = 2)
        self.wait(2)
        vector_arrow_b = Vector([2, 3], tip_length = 0.15).set_stroke(width=2)
        vector_b = MathTex(r"\vec{b}").move_to(axes.c2p(2.3, 3))
        self.play(Create(vector_arrow_b), run_time = 2)
        self.play(Write(vector_b), run_time = 2)
        self.wait(2)

        # projection calculation
        a = np.array([1, 0.2])
        b = np.array([2, 3])

        proj = (np.dot(b, a) / np.dot(a, a)) * a
        projection_vector = Vector(proj, color = YELLOW, tip_length=0.15)
        projection_vector.set_stroke(width=2)

        drop_line = DashedLine(
            vector_arrow_b.get_end(),
            projection_vector.get_end(),
            dashed_ratio=0.3
        )

        self.play(Create(drop_line), run_time = 4)
        self.play(Create(projection_vector), run_time=4)
        self.wait(2)
        projection_xa = MathTex(r"x\vec{a}").move_to(axes.c2p(2.5, 0.1))

        self.play(Write(projection_xa), run_time = 4)
        self.wait(2)
