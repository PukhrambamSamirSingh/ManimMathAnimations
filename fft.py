from manim import *

class FFT(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-3, 7, 1),
            y_range=(-3, 3, 1),
            x_length=11,
            y_length=7,
            tips=False
        )
        self.play(Create(axes), run_time=2)
        def fft_func1():
            return ParametricFunction(
                lambda t: axes.c2p(
                    t,
                    np.sin(2 * PI * t)
                ),
                t_range=(0, 7)
            ).set_stroke(width=2, color=YELLOW)
        
        def fft_func2():
            return ParametricFunction(
                lambda t: axes.c2p(
                    t,
                    np.cos(2 * PI * t)
                ),
                t_range=(0, 7)
            ).set_stroke(width=2, color=GREEN)
        
        def fft_product():
            return ParametricFunction(
                lambda t: axes.c2p(
                    t,
                    np.sin(2 * PI * t) * np.cos(2 * PI * t)
                ),
                t_range=(0, 7)
            ).set_stroke(width=2, color=ORANGE)
        
        func1 = fft_func1()
        func2 = fft_func2()
        func3 = fft_product()
        self.play(Create(func1), run_time=3)
        self.wait(2)
        self.play(Uncreate(func1), run_time=3)
        self.wait(1)
        self.play(Create(func2), run_time=3)
        self.wait(2)
        self.play(Uncreate(func2), run_time=3)
        self.wait(1)
        self.play(Create(func3), run_time=4)
        self.wait(2)