from turtle import Turtle 
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(x=-20, y=275)
        self.write(f"Score: 0, Highscore: {self.highscore}", align="center", font=("Arial", 20, "normal"))
        self.score = 0

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}", align="center", font=("Arial", 20, "normal"))
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        

            


        