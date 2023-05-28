from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which ninja turtle do you believe will win the race? "
                                                          "Enter a color: ")
# colors = ["red", "orange", "purple", "blue", "green", "black"]

ninja_turtles = {
    "blue": "Leonardo",
    "red": "Raphael",
    "purple": "Donatello",
    "orange": "Michelangelo",
}

colors = list(ninja_turtles.keys())
all_turtles = []

y_starting_pos = -130

# for i in range(len(colors)):
for i in range(len(ninja_turtles)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_starting_pos)
    y_starting_pos += 50
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            winner = ninja_turtles[winning_color]
            if winning_color == user_bet:
                # print(f"You've won! The {winning_color} turtle is the winner!")
                print(f"You've won! The {winner} is the winner!")
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                print(f"You've lost! {winner} is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
