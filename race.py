import turtle
import random

wn = turtle.Screen()

names = ['alex', 'jimmy', 'mary', 'luci', 'peter']
colors = ['red', 'green', 'yellow', 'orange', 'blue']
y_position = [-100, -50, 0, 50, 100]
i = 0

for j in range(len(names)):
    names[j] = turtle.Turtle()

for turtle in wn.turtles():
    turtle.shape('turtle')
    turtle.up()
    turtle.color(colors[i])
    turtle.goto(x=-300, y=y_position[i])
    i += 1


def main():
    user_bet = wn.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    if user_bet:
        is_race_on = True
        while is_race_on:

            for turtle in wn.turtles():
                if turtle.xcor() >= 300:
                    is_race_on = False
                    winner = turtle.pencolor()
                    if user_bet == winner:
                        print(f"You Won! {winner.capitalize()} turtle was the winner!")
                    else:
                        print(f"You Lose. {winner.capitalize()} turtle was the winner.")

                turtle.speed(random.randint(1, 7))
                turtle.forward(random.randint(1, 10))
    else:
        print("Enter a bet to start the game.")
        wn.bye()


main()
