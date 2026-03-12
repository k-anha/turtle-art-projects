# Python code for drawing hexagon logo

import shapes
import turtle

t: object = turtle.Turtle()

t.speed(5)
colors: list[str] = [
    "red",
    "purple",
    "indigo",
    "turquoise",
    "green",
    "yellow",
]
t.pensize(10)
size: int = 200
gap: int = 10
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
        base1=size*2,
        base2=(size*2) / 2,
        leg=(size*2) / 2,
        fill_color=colors[i],
        pen_color="white",
        fill_shape=True,
    )


turtle.exitonclick()
