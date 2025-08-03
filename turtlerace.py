from turtle import Turtle, Screen
import random
race_on = False
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Bet", prompt="Enter a colour")
num_turtles = 6

for i in range(num_turtles):
    t = Turtle(shape="turtle")
    t.color(colours[i])
    turtles.append(t)
    
for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].goto(x=-235, y=100 - i*30)
    
if bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 230:
            race_on = False
            win_color = t.pencolor()
            if win_color == bet:
                print(f"You win, the winning colour was {win_color}")
            else:
                print(f"You lose, the winning colour was {win_color}")
                
        t.forward(random.randint(0, 10))
    

screen.exitonclick()
