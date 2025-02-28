from turtle import Turtle, Screen
tom = Turtle()
tom.color("red")

for steps in range(100):
    for c in ("red", "blue", "green"):
        tom.color(c)
        tom.forward(steps)
        tom.right(25)

print(tom)

screen = Screen()
screen.exitonclick()