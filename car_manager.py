from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.create_car()
        
    def move_all(self):
        for i in range(len(self.cars)):
            self.move(self.cars[i])
    
    def move(self, t):
        t.goto(t.xcor() - STARTING_MOVE_DISTANCE, t.ycor())
        
    def create_car(self):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.color(random.choice(COLORS))
        t.goto(250, random.randint(-220, 280))
        self.cars.append(t)