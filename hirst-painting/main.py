import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
t.hideturtle()
t.penup()
t.setposition(-300, -300)
t.hideturtle()
screen = Screen()
t.hideturtle()
screen.colormode(255)
color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28), (10, 98, 50), (166, 181, 232), (237, 170, 159), (253, 5, 42), (9, 87, 103), (21, 35, 249), (63, 100, 8), (253, 9, 5), (0, 246, 244), (0, 250, 254)]
circle_width = 20
space = 50
y = -300
turtle.penup()



def random_color_choice():
    random_color = random.choice(color_list)
    return random_color


def draw_dot():
    for j in range(10):
        t.dot(circle_width, random_color_choice())
        t.forward(space)


for i in range(10):
    if i == 0:
        draw_dot()
    if i >= 1:
        y += 50
        t.setposition(-300, y)
        draw_dot()

screen.exitonclick()
