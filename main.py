from question_model import QuestionModel
from data import question_data as qd
from quiz_brain import QuizBrain as qb

question_bank = []

for index in range(len(qd)):
    text = qd[index]["question"]
    answer = qd[index]["correct_answer"]
    new_q = QuestionModel(text, answer)
    question_bank.append(new_q)
    
quiz = qb(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've Completed the Quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
