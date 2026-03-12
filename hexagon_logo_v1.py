# Python code for drawing hexagon logo

import shapes
import turtle

t = turtle.Turtle()

t.speed(10)
colors: list[str] = [
    "purple",
    "indigo",
    "turquoise",
    "green",
    "yellow",
    "red",
]

t.pu()
t.rt(150)
t.fd(90)
t.pd()
x, y = t.pos()
base: int = 90
for i in range(1, 7):
    shapes.draw_regular_trapezoid(
        x,
        y,
        ttl=t,
        base1=base,
        base2=base / 2,
        leg=base / 2,
        direction=(i * 60) + 30,
        pen_color="white",
        fill_color=colors[i - 1],
        fill_shape=True,
    )
    t.pu()
    t.fd(base / 2)
    t.pd()
    x, y = t.pos()
turtle.exitonclick()
