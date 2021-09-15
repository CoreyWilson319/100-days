from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue",]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
starting_x = -230
starting_y = -80

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race enter a color")

is_race_on = False

for _ in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(_)
    new_turtle.setposition(x=starting_x, y=starting_y)
    turtles.append(new_turtle)
    starting_y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for _ in turtles:
        if _.xcor() > 230:
            is_race_on = False
            winning_color = _.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = randint(0, 10)
        _.forward(rand_distance)





screen.exitonclick()