from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which ninja turtle do you believe will win the race? "
                                                          "Enter a color: ")
colors = ["red", "orange", "purple", "blue", "green", "black"]

y_starting_pos = -130

for i in range(len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_starting_pos)
    y_starting_pos += 50


screen.exitonclick()
