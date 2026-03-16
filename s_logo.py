#import necessary modules

import shapes
import turtle
t=turtle.Turtle()
t.teleport(20,0)
t.lt(90)
t.fd(60)
for _ in range(4):
    t.rt(60)
    t.fd(60)
t.rt(60)
t.fd(30)
t.setheading(90)
t.fd(40)
t.rt(120)
t.fd(30)
t.lt(60)
for _ in range(4):
    t.fd(20)
    t.lt(60)
turtle.exitonclick()