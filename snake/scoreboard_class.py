'''Scoreboard Class'''
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open("data.txt", mode="r") as f:
                content = f.read().strip()
                if content: 
                    self.high_score = int(content)
                else:
                    self.high_score = 0
        except FileNotFoundError:
            
            self.high_score = 0
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color('white')
        
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('arial',24,'normal'))

    def increase_score(self):
        self.score += 1
        
        self.update_scoreboard()
    '''def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('arial',24,'normal'))'''
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',mode='w') as f:
                f.write(f"{self.high_score}") #has to be str
            
        self.score = 0
        '''self.clear()'''
        self.update_scoreboard()