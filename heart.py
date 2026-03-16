import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(3)

# Start drawing heart
pen.begin_fill()

pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()

# Hide turtle
pen.hideturtle()

turtle.done()