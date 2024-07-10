import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle named "drawer"
drawer = turtle.Turtle()
drawer.color("black")
drawer.pensize(2)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        drawer.forward(size)
        drawer.right(90)

# Draw a square with side length 100
draw_square(100)

# Hide the turtle and display the window
drawer.hideturtle()
wn.mainloop()
