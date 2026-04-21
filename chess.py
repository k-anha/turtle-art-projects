
import turtle


def draw_board(turtle:turtle.Turtle)->None:
    """Draws the chess board using turtle graphics."""
    # Code to draw the chess board goes here
    SIZE :int = 400  # Size of the chess board
    SQUARE_SIZE :int = SIZE // 8  # Size of each square
    turtle.teleport(-SIZE // 2, SIZE // 2)  # Start at the top-left corner of the board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"
            turtle.fillcolor(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(SQUARE_SIZE)
                turtle.right(90)
            turtle.end_fill()
            turtle.forward(SQUARE_SIZE)
        turtle.backward(SQUARE_SIZE * 8)
        turtle.right(90)
        turtle.forward(SQUARE_SIZE)
        turtle.left(90)

def main()->None:
    """Main function to set up the turtle and draw the chess board."""
    screen = turtle.Screen()
    screen.title("Turtle Chess Board")
    chess_turtle :turtle.Turtle = turtle.Turtle()
    chess_turtle.speed(0)  # Set the turtle speed to the fastest
    draw_board(chess_turtle)
    screen.exitonclick()  # Wait for a click to exit

if __name__ == "__main__":
    main()