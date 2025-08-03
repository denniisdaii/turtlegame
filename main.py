import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "w")
game_is_on = True
count = 1
while game_is_on:
    time.sleep(0.1 / (scoreboard.level + 1))
    screen.update()
    for i in range(len(car_manager.cars)):
        if player.distance(car_manager.cars[i]) < 30:
            game_is_on = False
            scoreboard.game_over()
    if count % 5 == 0:
        car_manager.create_car()
    
    car_manager.move_all()
    if player.check_pos():
        player.reset_pos()
        scoreboard.next_level()
        scoreboard.write_level()
    count+=1


screen.exitonclick()