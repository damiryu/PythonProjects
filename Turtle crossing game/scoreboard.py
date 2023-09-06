from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super(). __init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.goto(-220, 260)
        self.write(f"level: {self.level}", align=ALIGN, font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)


