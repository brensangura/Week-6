import turtle
import colorsys

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
screen = turtle.Screen()
screen.bgcolor("black")  # Black background
t.pensize(2)

# Generate a spiral with color gradients
for i in range(360):
    # Convert hue to RGB for smooth color transitions
    color = colorsys.hsv_to_rgb(i / 360, 1.0, 1.0)
    t.pencolor(color)
    t.forward(i * 0.1)  # Move forward, increasing slightly
    t.left(59)  # Turn to create spiral effect

turtle.done()
