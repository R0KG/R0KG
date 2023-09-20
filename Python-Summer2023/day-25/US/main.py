from turtle import *
import pandas as pd
import csv

def get_mouse_click_coor(x,y):
    pen = Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto(x,y)
    pen.pendown()
    pen.write(f"Text at {x},{y}", font=("Times New Roman", 12, "normal"))
    print(x,y)
    done()
    
    
screen = Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
shape("blank_states_img.gif")
states_data = pd.read_csv("50_states.csv")
playing = True
score = 0
states_list = []
all_states = states_data.state.to_list()
while playing:
    answer_state = screen.textinput(title=f"Guess the State {score}/50",prompt="What's anoter state's name? ").title()
    if answer_state in states_list:
        playing = False
    else:
        if answer_state in all_states:
            score += 1     
            state_data = states_data[states_data.state == answer_state]
            x = state_data.x
            y = state_data.y
            pen = Turtle()
            pen.penup()
            pen.hideturtle()
            pen.goto(int(x.iloc[0]),int(y.iloc[0]))
            pen.pendown()
            pen.write(answer_state)
        else:
            playing = False
            
    if score > 50:
        playing = False
    states_list.append(answer_state)

bye()

screen.mainloop()