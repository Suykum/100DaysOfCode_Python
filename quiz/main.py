from quiz.question_model import Question
from quiz.data import question_data
from quiz.quiz_brain import QuizBrain

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")