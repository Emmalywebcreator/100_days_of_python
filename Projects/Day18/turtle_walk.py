# turtle make a random walk
import random
from turtle import Turtle, Screen

screen = Screen()
jimmy = Turtle()
jimmy.pensize(15)
jimmy.speed("fastest")

colors = ["red", "blue", "green", "orange", "purple", "yellow", "violet", "magenta", "deep pink"]
direction = [0, 90, 180, 270]

for _ in range(200):
    jimmy.color(random.choice(colors))
    jimmy.forward(30)
    jimmy.right(random.choice(direction))


screen.exitonclick()