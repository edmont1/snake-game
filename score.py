from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.penup()
        self.hideturtle()
        self.setpos(100, 260)
        self.color('white')
        self.high_score = 0
        self.scoreboard()


    def scoreboard(self):
        try:
            with open('highscore.txt',mode='r') as hs:
                self.high_score = hs.read()
        except FileNotFoundError:
            with open('highscore.txt', mode='w') as hs:
                hs.write('0')
        self.clear()
        self.goto(100, 260)
        self.write(arg=f'SCORE: {self.value} HIGH SCORE : {self.high_score}', font=('Courier', 20, 'normal'),align='center')

    def scorecount(self):
        self.value += 1
        self.scoreboard()


    def gameover(self):
        self.setpos(0,0)
        self.write(arg=f'GAME OVER.', font=('Courier', 20, 'normal'), align='center')


    def set_high_score(self):
        if self.value > int(self.high_score):
            with open('highscore.txt',mode='w') as hs:
                hs.write(str(self.value))
        self.value = 0
        self.scoreboard()

