from quiz.question_model import Question
from quiz.data import question_data
from quiz.quiz_brain import QuizBrain
from quiz.ui import QuizInterface

question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()
print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")