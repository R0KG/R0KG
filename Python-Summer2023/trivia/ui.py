import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,questions : QuizBrain):
        self.score = 0
        self.questions = questions
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background="#375362")
        self.score_label = tk.Label(text="Score: 0",highlightthickness=0,background="#375362",foreground=("white"))
        self.score_label.grid(column=1,row=0)
        self.canvas = tk.Canvas(width= 300,height=250,bg= "white")
        self.canvas_text = self.canvas.create_text(150,
                                              125,
                                              width= 280,
                                              text="Some question",
                                              fill=THEME_COLOR,
                                              font=("Arial",20,"italic")
                                              )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        right_img = tk.PhotoImage(file="images/true.png")
        wrong_image = tk.PhotoImage(file="images/false.png")
        right_button = tk.Button(image=right_img,command= self.right_button)
        right_button.grid(row=2,column=0)
        wrong_button = tk.Button(image=wrong_image,command= self.wrong_button)
        wrong_button.grid(row=2,column=1)       
        self.get_next_question()
            
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.questions.next_question()
        self.canvas.itemconfig(self.canvas_text,text=q_text)
    def right_button(self):
        if  self.questions.check_answer("True") == True:
            self.score_label.config(text= f"Score:{self.questions.score}")
            
        self.get_next_question()
    def wrong_button(self):
        if  self.questions.check_answer("True") == True:
            self.score_label.config(text= f"Score:{self.questions.score}")
        self.get_next_question()
    

