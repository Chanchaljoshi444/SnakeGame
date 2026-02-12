from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("grey")
        self.ht()
        self.penup()
        self.goto(0,272)
        self.display_score()


    def display_score(self):
        self.write(f"Score: {self.score} ", move=False, align='center', font=('Arial', 18, 'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.clear()
        self.ht()
        self.penup()
        self.goto(0,0)
        self.write(f" Game Over!\nFinal score: {self.score} ", move=False, align='center', font=('Arial', 18, 'bold'))

