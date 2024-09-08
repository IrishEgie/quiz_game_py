class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q_number = self.question_list[self.question_number]
        self.question_number+=1
        q_answer = input(f"Q.{self.question_number}: {q_number.text} (True/False)?: ").lower()
        self.check_answer(q_answer, q_number.answer, self.question_number)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer, correct_answer, question_number):
        if answer == correct_answer.lower():
            print("You got it Right!")
            self.score+=1
            print(f"Your current score: {self.score}/{question_number}")
        else: 
            print(f"That is Wrong!")
            print(f"Your current score: {self.score}/{question_number}")
        print(f"The correct answer was: {correct_answer}\n")
            