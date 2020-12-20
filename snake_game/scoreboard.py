from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE = "data.txt"


def read_saved_score():
    with open(FILE) as file:
        return file.read()


def write_score_to_file(score):
    with open(FILE, "w") as file:
        file.write(str(score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.high_score = int(read_saved_score())
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        write_score_to_file(self.high_score)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

