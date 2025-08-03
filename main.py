from turtle import Turtle, Screen

t = Turtle()

def move_forwards():
    t.forward(10)
    
def move_backwards():
    t.backward(10)
    
def anticlocKwise():
    t.setheading(t.heading() + 5)

def clockwise():
    t.setheading(t.heading() - 5)
    
def clear():
    t.reset()   
screen = Screen()

screen.listen()
def keypress(func, input):
    screen.onkeypress(func, input)
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(anticlocKwise, "a")
screen.onkeypress(clockwise, "d")
screen.onkeypress(clear, "c")

screen.exitonclick()