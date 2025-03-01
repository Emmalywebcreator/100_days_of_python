from turtle import Turtle, Screen
tom = Turtle()
tom.color("red")

for steps in range(100):
    for c in ("red", "blue", "green"):
        tom.color(c)
        tom.forward(steps)
        tom.right(25)
        
# tom.speed("fastest")

# colors = ["red", "blue", "green", "purple", "yellow"]

# for steps in range(100):
#     tom.color(colors[steps % len(colors)])
#     tom.forward(steps)
#     tom.right(45)

print(tom)

screen = Screen()
screen.exitonclick()