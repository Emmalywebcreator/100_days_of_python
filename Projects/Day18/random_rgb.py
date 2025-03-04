# turtle make a random walk with random rgb
import random
import turtle as t

screen = t.Screen()
t.colormode(255)
jimmy = t.Turtle()
jimmy.pensize(15)
jimmy.speed("fastest")

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]

for _ in range(200):
    jimmy.color(random_colors())
    jimmy.forward(30)
    jimmy.right(random.choice(direction))
    


screen.exitonclick()