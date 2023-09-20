from question_model import Question
class QuizBrain:
    def __init__(self,qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
        
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False    
        
    def ask_user(self):
        answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number].text} (True/False)?: ")
        if self.check_answer(self.question_number,answer):
            print("You re right")
            self.score += 1
        else:
            print("You re wrong")
        self.question_number += 1
    
    def check_answer(self,question_number,answer):
        if self.question_list[question_number].answer.lower() == answer.lower():
            return True
        else:
            return False
    
    
        