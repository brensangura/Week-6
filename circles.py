import colorsys
import turtle
import time

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")

for i in range(100):
    t.pencolor("white")
    t.circle(50 + i % 20)  # Vary circle size
    t.left(10)
    screen.update()
    time.sleep(0.05)  # Slow it down for animation
    t.clear()  # Clear to redraw

turtle.done()


t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")

for i in range(200):
    color = colorsys.hsv_to_rgb(i / 200, 1.0, 1.0)
    t.pencolor(color)
    t.circle(100 - i * 0.5)  # Shrink circles for "depth"
    t.left(45)
    t.up()
    t.forward(10)
    t.down()

turtle.done()
