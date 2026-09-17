from manim import *
import numpy as np

config.pixel_width = 1024
config.pixel_height = 768
config.frame_width = 12
config.frame_height = 9
config.background_color = BLACK


class RoseForYou(ThreeDScene):

    @staticmethod
    def rose_point(x, theta):
        phi = (PI / 2) * np.exp(-theta / (8 * PI))

        X = 1 - 0.5 * (
            (5 / 4) *
            (1 - np.mod(3.6 * theta, 2 * PI) / PI) ** 2
            - 1 / 4
        ) ** 2

        y = (
            1.95653
            * x ** 2
            * (1.27689 * x - 1) ** 2
            * np.sin(phi)
        )

        r = X * (
            x * np.sin(phi)
            + y * np.cos(phi)
        )

        return np.array([
            r * np.sin(theta),
            r * np.cos(theta),
            X * (
                x * np.cos(phi)
                - y * np.sin(phi)
            ),
        ])

    def construct(self):
        self.set_camera_orientation(
            phi=62 * DEGREES,
            theta=-55 * DEGREES,
            gamma=0 * DEGREES,
            zoom=1.0,
        )

        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-2.5, 2.5, 1],
            x_length=7.0,
            y_length=7.0,
            z_length=7.0,
            axis_config={
                "color": WHITE,
                "stroke_width": 1.0,
                "include_ticks": True,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
        )

        self.add(axes)

        rose = Surface(
            lambda x, theta: self.rose_point(x, theta),
            u_range=[0, 1],
            v_range=[-2 * PI, 21 * PI],
            resolution=(36, 180),
            fill_color="#F22558",
            fill_opacity=1.0,
            checkerboard_colors=False,
            stroke_color="#F0B33E",
            stroke_width=0.45,
        )

        rose.scale(2.55)

        self.play(
            Create(rose),
            run_time=5.0,
            rate_func=smooth,
        )

        self.wait(0.8)

        self.move_camera(
            phi=90 * DEGREES,
            theta=0 * DEGREES,
            gamma=0 * DEGREES,
            zoom=1.0,
            run_time=4.0,
            rate_func=smooth,
        )

        self.wait(1.0)

        self.move_camera(
            phi=8 * DEGREES,
            theta=0 * DEGREES,
            gamma=0 * DEGREES,
            zoom=1.0,
            run_time=4.0,
            rate_func=smooth,
        )

        self.wait(1.0)
