# Python code for drawing hexagon logo

import shapes
import turtle


def draw_hexagon_logo(speed: int = 5, length: int = 200, gap: int = 10):
    t: object = turtle.Turtle()

    t.speed(speed)
    colors: list[str] = [
        "red",
        "purple",
        "indigo",
        "turquoise",
        "green",
        "yellow",
    ]
    t.pensize(gap)
    size: int = length
    base: float = (size / 2) * pow(3, 1 / 2)
    height: float = size / 2

    co_ordinates: list[tuple] = [
        (-base, height),
        (0, (height * 2)),
        (base, height),
        (base, -height),
        (0, -(height * 2)),
        (-base, -height),
    ]

    for i in range(6):
        shapes.draw_regular_trapezoid(
            *co_ordinates[i],
            direction=30 - (i * 60),
            ttl=t,
            base1=size * 2,
            base2=(size * 2) / 2,
            leg=(size * 2) / 2,
            fill_color=colors[i],
            pen_color="white",
            fill_shape=True,
        )

    turtle.exitonclick()


draw_hexagon_logo()
