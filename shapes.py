# Shapes in python using turtle art graphics

# importing turtle module
import turtle
import math


# Drawing rectangle with length, width
def draw_rectangle(
    x: float = 0,
    y: float = 0,
    length: float = 100,
    width: float = 50,
    direction: float = 0,
    pen_color: str = "black",
    fill_color: str = "black",
    ttl: turtle.Turtle | None = None,
    fill_shape: bool = False,
) -> None:
    if ttl is None:
        ttl = turtle.Turtle()
    ttl.pu()
    ttl.goto(x, y)
    ttl.pd()
    ttl.setheading(direction)
    ttl.pencolor(pen_color)
    ttl.fillcolor(fill_color)

    if fill_shape:
        ttl.begin_fill()
    for _ in range(2):
        ttl.fd(length)
        ttl.rt(90)
        ttl.fd(width)
        ttl.rt(90)
    if fill_shape:
        ttl.end_fill()


# Python code to draw square
def draw_square(
    x: float = 0,
    y: float = 0,
    length: float = 100,
    direction: float = 0,
    pen_color: str = "black",
    fill_color: str = "black",
    ttl: turtle.Turtle | None = None,
    fill_shape: bool = False,
) -> None:
    draw_polygon(
        x=x,
        y=y,
        direction=direction,
        length=length,
        sides=4,
        ttl=ttl,
        pen_color=pen_color,
        fill_color=fill_color,
        fill_shape=fill_shape,
    )


# Python code to draw rhombus
def draw_rhombus(
    x: float = 0,
    y: float = 0,
    direction: float = 0,
    min_angle: float = 60,
    length: float = 100,
    ttl: turtle.Turtle | None = None,
    pen_color: str = "black",
    fill_color: str = "black",
    fill_shape: bool = False,
) -> None:
    if ttl is None:
        ttl = turtle.Turtle()

    ttl.pu()
    ttl.goto(x, y)
    ttl.pd()
    ttl.setheading(direction)
    ttl.pencolor(pen_color)
    ttl.fillcolor(fill_color)
    if fill_shape:
        ttl.begin_fill()
    for i in range(4):
        ttl.fd(length)
        if i % 2 == 0:
            ttl.rt(min_angle)
        else:
            ttl.rt(180 - min_angle)
    if fill_shape:
        ttl.end_fill()


# Python code to draw any polygon
def draw_polygon(
    x: float = 0,
    y: float = 0,
    direction: float = 0,
    length: float = 60,
    sides: int = 5,
    ttl: turtle.Turtle | None = None,
    pen_color: str = "black",
    fill_color: str = "black",
    fill_shape: bool = False,
) -> None:
    if ttl is None:
        ttl = turtle.Turtle()

    ttl.pu()
    ttl.goto(x, y)
    ttl.pd()
    ttl.setheading(direction)
    ttl.pencolor(pen_color)
    ttl.fillcolor(fill_color)
    if fill_shape:
        ttl.begin_fill()

    angle = 360 / sides
    for _ in range(sides):
        ttl.forward(length)
        ttl.left(angle)

    if fill_shape:
        ttl.end_fill()


def draw_regular_trapezoid(
    x: float = 0,
    y: float = 0,
    direction: float = 0,
    base1: float = 100,
    base2: float = 60,
    leg:float=40,
    ttl: turtle.Turtle | None = None,
    pen_color: str = "black",
    fill_color: str = "black",
    fill_shape: bool = False,
)-> None:
    # \theta =\arccos \left( \frac{b_1-b_2}{2l}\right) 

    theta_degrees_1:float=math.degrees(math.acos(abs(base1-base2)/(2*leg)))
    if ttl is None:
        ttl=turtle.Turtle()
    ttl.pu()
    ttl.goto(x,y)
    ttl.pd()
    ttl.setheading(direction)
    ttl.color(pen_color,fill_color)
    if fill_shape:
        ttl.begin_fill()
    
    ttl.fd(base1)
    ttl.left(180-theta_degrees_1)
    ttl.fd(leg)
    ttl.left(theta_degrees_1)
    ttl.fd(base2)
    ttl.left(theta_degrees_1)
    ttl.fd(leg)
    
    if fill_shape:
        ttl.end_fill()