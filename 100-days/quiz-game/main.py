from quiz_data import question_data
from question_class import Question
from quiz_ops import Quiz
print(f"Welcome to this {len(question_data)} question long aviation quiz!")
question_bank = []
for q in question_data:
    question_text = q['text']
    question_answer = str(q['answer'])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
#print(len(question_bank))
quiz = Quiz(question_bank) #question_bank acting as q_list
while quiz.still_has_questions():
    quiz.next_question()
    
print(f"Quiz Complete!\nYour final score is {quiz.score} / 42")