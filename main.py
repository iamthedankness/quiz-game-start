from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for item in question_data:
    new_question=Questions(item["question"],item["correct_answer"])
    question_bank.append(new_question)

quiz= QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    print("\n")
current_score= quiz.score
total= quiz.question_number
print(f"You have complete the quiz\n Your final score is {current_score}/{total}")