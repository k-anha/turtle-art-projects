#Turtle arts shapes and its projects
##shapes.py

<p>This is a lightweight python library for basic shapes.
This library includes a polygon function which can be used to make any regular polygon shape</p>

**<p>All of function to draw shapes includes some common syntaxes as:</p>**

```
    x: float = 0,
    y: float = 0,
    direction: float = 0,
    ttl: turtle.Turtle | None = None,
    pen_color: str = "black",
    fill_color: str = "black",
    fill_shape: bool = False,
```

* Here `x` is a float point which represent **"x" co-ordinated** in python turtle graphics.
* Similary there is `y` which represents **"y" co-ordinated** in python turtle graphics
* There is **direction** which is face of turtle. You can set it in python turtle degrees to change turtle face accordingly
* **ttl** parameter represents turtle object which will be created by you if not given function will create it's own turtle
* **pen_color** and **fill_color** both are color names of python turtle for pen color and fill color respectively
* **fill_shape** is a boolean value if True then shape will be filled accordingly.

</p>

```
    #python code to draw triangle

    import shapes
    shapes.draw_polygon(length=60,sides=3)

    #will draw an equilateral triangle

```


</p>
