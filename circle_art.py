import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
t.pensize(2)

for i in range(180):
    color = colorsys.hsv_to_rgb(i / 180, 1.0, 1.0)
    t.pencolor(color)
    t.circle(50 + i * 2, 90)  # Draw quarter-circle arcs
    t.left(73)  # Unique angle for overlapping patterns

turtle.done()
