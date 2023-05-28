from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which ninja turtle do you believe will win the bet? "
                                                          "Enter a color: ")
tim = Turtle()


screen.exitonclick()
