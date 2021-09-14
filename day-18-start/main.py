from turtle import Turtle, Screen
from random import choice, randint

turtle = Turtle()

# divide 360 by the number of side to get the angle of a shape

turtle.pensize(1)
turtle.speed("fastest")

screen = Screen()
screen.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

def random_walk():
    directions = [0, 90, 180, 270]
    turtle.pencolor(random_color())
    direction = choice(directions)
    turtle.forward(30)
    turtle.setheading(direction)


def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 10)





screen.exitonclick()