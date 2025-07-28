import turtle
import pandas as pd

# Load the data
data = pd.read_csv("clicked_coordinates.csv")

count = 0

turtle.penup()
turtle.hideturtle()
game_on = True

# Set up the screen

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(width=713, height=837)
screen.bgpic("inde52.gif")  # Use as background

#remeber state
states = list(data.State)
remember_state = list()

def learn():
    forgotten_state = [state for state in states if state not in remember_state]
    df = pd.DataFrame(forgotten_state)
    df.to_csv("forget_states.csv",index=False)

    read = pd.read_csv("forget_states.csv")
    print(read)

while game_on:
    answer_state = turtle.textinput(title = f"{count}/{len(states)} Correct State:",prompt="What's another state's name ?").title()

    if answer_state in states and answer_state not in remember_state:
        row = data[data.State == answer_state]
        x = row.X.values[0]
        y = row.Y.values[0]
        turtle.goto(x,y)
        turtle.write(answer_state,align="center",font=("Arial",10,"normal"))
        count += 1
        remember_state.append(answer_state)

    if count==len(states) or answer_state=="Exit":
        game_on = False
        if answer_state == "Exit":
            print("------------Learn this states------")
            learn()





