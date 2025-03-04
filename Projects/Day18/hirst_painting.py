import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.back(230)
tim.seth(-90)
tim.forward(220)
tim.seth(0)

num_dots = 100
cols = 10


color_list = [(208, 157, 105), (215, 218, 228), (236, 214, 225), (141, 145, 160), (184, 70, 27), (227, 211, 115), (95, 105, 138), (191, 158, 26), (220, 234, 224), (202, 148, 175), (9, 18, 62), (97, 115, 175), (190, 17, 4), (13, 31, 14)]

for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % cols == 0:
        tim.seth(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.seth(0)

screen = t.Screen()
screen.exitonclick()