#Python code for petal shaped logo

import shapes

def draw_petal_logo():
    import turtle
    t=turtle.Turtle()
    for i in range(3):
        shapes.draw_rhombus(ttl=t,direction=i*(360/3),fill_shape=True)
    t.ht()
    turtle.exitonclick()
    
draw_petal_logo()