import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
dic_count = {"Break" : 0,
             "Work": 0,
             "Long Break" : 0}
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text= "Timer",font= (FONT_NAME,50,"bold"),bg= YELLOW, fg= GREEN)
    canvas.itemconfig(timer_text,text= "00:00")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    global dic_count
    if reps % 8 == 0:
        timer_label.config(text= "Big Break", fg= PINK)
        dic_count["Long Break"] += 1
        count_down(20 * 60)
    elif reps % 2 == 0:
        timer_label.config(text= "Small Break", fg= PINK)
        dic_count["Break"] += 1
        count_down(5 * 60)
    elif  reps % 2 == 1:
        dic_count["Work"] += 1
        timer_label.config(text= "Work", fg= PINK)
        count_down(25 * 60)

        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        temp = ""
        for i in range (dic_count["Work"]):
            temp += "✔"
        checkmark.config(text= temp)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW)

timer_label = tk.Label(text= "Timer",font= (FONT_NAME,50,"bold"),bg= YELLOW, fg= GREEN)

tomato_img = tk.PhotoImage(file= "tomato.png")
canvas = tk.Canvas(height= 224, width= 200,bg= YELLOW, highlightthickness= 0)
canvas.create_image(100,112, image= tomato_img )
timer_text = canvas.create_text(100,130, text= "00:00",fill= "white", font= (FONT_NAME,35,"bold"))
start_but = tk.Button(text= "Start",padx= 30,height= 1,width=1, command= start_timer) 
reset_but = tk.Button(text= "Reset",padx= 30,height= 1,width=1,command= reset)
checkmark = tk.Label(bg=YELLOW,highlightthickness= 0)
checkmark.grid(column= 1,row= 5)
start_but.grid(column= 0,row= 4)
reset_but.grid(column= 2,row= 4)
timer_label.grid(column= 1,row= 0)
canvas.grid(column= 1, row= 3)








window.mainloop()