class QuizBrain:
    def __init__(self, question_list):
        self.question_list=question_list
        self.question_number=0
        self.score=0

    def next_question(self):
        question= self.question_list[self.question_number]
        self.question_number+=1
        user_choice = input(f"Q{self.question_number}: {question.text} True or False").lower()
        correct_answer=question.answer
        self.check_answer(user_choice,correct_answer)
    def check_answer(self,user_choice,correct_answer):
        if user_choice.lower() ==correct_answer.lower():
            self.score+=1
            print(f"You answer is right,")
        else:
            print("Your answer is wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Current Score is  {self.score}/{self.question_number}")



    def still_has_question(self):
        return self.question_number< len(self.question_list)

