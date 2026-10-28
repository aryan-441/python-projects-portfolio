class Quiz:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
    def still_has_questions(self):
        return self.q_number < len(self.q_list)
       
    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"Q{self.q_number}: {current_q.text} (True / False)").capitalize()
        self.check_answer(answer, current_q.answer)
    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("That's incorrect!")
            print(f"The correct answer is {correct_answer}")
        print(f"Current score: {self.score}/{self.q_number}")


