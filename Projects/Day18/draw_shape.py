from turtle import Turtle, Screen
import random

jimmy = Turtle()
jimmy.pensize(4)
jimmy.speed("fastest")
screen = Screen()

colors = ["red", "blue", "green", "orange", "purple", "yellow", "violet", "magenta", "deep pink"]

def draw_shape(sides):
    """Draws a shape with a given number of sides."""
    angle = 360 / sides
    for _ in range(sides):
        jimmy.color(random.choice(colors))
        jimmy.forward(70)
        jimmy.right(angle)

for no_sides in range(3, 11):
    draw_shape(no_sides)

screen.exitonclick()