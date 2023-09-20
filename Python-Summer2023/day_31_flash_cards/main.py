import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
#Words fro Data Base
progress_dict = {}
data = pd.read_csv("Unbenannte Tabelle - Tabellenblatt1 (2).csv")
words_dic = {row.German : row.English for (ind, row) in data.iterrows()}
to_learn = data.to_dict(orient="records")
current_card = {}
#Turning the card
def turn_card_to_german():
    global random_german,current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image,image= card_front_image)
    canvas.itemconfig(language, text= "German",fill= "black")
    canvas.itemconfig(canvas_word, text= current_card["German"],fill="black")
    window.after(3000,func=turn_card_to_eng)
    
def wrong_func():
    turn_card_to_german()
def right_func():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("words_to_learn.csv",index=False)

    turn_card_to_german()
def turn_card_to_eng():
    canvas.itemconfig(canvas_image,image= card_back_image)
    canvas.itemconfig(language, text= "English",fill= "white")
    canvas.itemconfig(canvas_word,text= current_card["English"],fill= "white")
    
    

# GUI Design
window = tk.Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50,bg= BACKGROUND_COLOR)
#Image
card_front_image = tk.PhotoImage(file= "card_front.png")
card_back_image = tk.PhotoImage(file= "card_back.png")
right_image = tk.PhotoImage(file= "right.png")
wrong_image = tk.PhotoImage(file= "wrong.png")
#Canvas
canvas = tk.Canvas(height= 526, width= 800, highlightthickness= 0,bg= BACKGROUND_COLOR)
canvas_image = canvas.create_image(400,263, image= card_back_image)

language = canvas.create_text(400,150,text= "English",fill="white", font= ("Ariel",40,"italic"))

random_german = random.choice(list(words_dic.keys()))
canvas_word = canvas.create_text(400,263,text= words_dic[random_german],fill="white", font= ("Ariel",60,"bold"))

canvas.grid(column= 0 ,row= 1,columnspan= 2)


#Buttons
right_button = tk.Button(image= right_image, highlightthickness= 0,command= right_func)
wrong_button = tk.Button(image= wrong_image, highlightthickness= 0,command= wrong_func)

right_button.grid(column= 1,row= 2)
wrong_button.grid(column= 0,row= 2)



















window.mainloop()