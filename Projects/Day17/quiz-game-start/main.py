from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)
    
quiz = QuizBrain(question_list=question_bank)
while quiz.still_have_question():
    quiz.next_question()
print("Congratulation on completing the quiz")
print(f"You scored {quiz.score} out of {quiz.question_number}")
if quiz.score >= 7:
    print("You did well!")
elif quiz.score >= 9:
    print("You are a genuis!")
else:
    print("You can do better")