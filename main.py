from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

tim_line = Turtle()
tim_line.penup()
tim_line.goto(x=225, y=200)
tim_line.pendown()
tim_line.pencolor("LightSeaGreen")
tim_line.pensize(5)
tim_line.right(90)
tim_line.forward(410)

race_is_on = False
racing_turtles = []

ok_answer_1 = False
while ok_answer_1 == False:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    if user_bet in colors:
        ok_answer_1 = True
        race_is_on = True

i = 0
for item in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(item)
    new_turtle.penup()
    new_turtle.goto(x=-225, y=(-100 + i))
    racing_turtles.append(new_turtle)

    i += 50

while race_is_on == True:
    for turtle in racing_turtles:

        if 225 <= turtle.xcor():
            print("Its over")

            print(f"Your bet was: {user_bet}")

            if str(turtle.color()[0]) == str(user_bet):
                print(turtle.color())
                print("You won :D")
            else:
                print(f"You lose :\. Winner turtle is {turtle.color()[0]}")

            race_is_on = False
        else:
            n_steps = random.randint(0, 25)
            turtle.forward(n_steps)

screen.exitonclick()
