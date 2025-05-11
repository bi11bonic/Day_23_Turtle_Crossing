import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")


scoreboard = Scoreboard()
player = Player()

car = CarManager()
car_list = car.car_list
car_list.append(car)
# CarManager.where_am_i()
cycle_counter = 0

screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # car.forward(1)
    cycle_counter += 1


    if cycle_counter == 10:
        car.add_car()
        # print(car_list)
        cycle_counter = 0


    for item in car_list:
        item.car_move()
        if item.xcor() < -320:
            # item.clear()
            car_list.remove(item)

        if player.distance(item) < 15:
            game_is_on = False
            # pass
        else:
            pass
    # for car in car_list:
    #     if player.distance(car) < 10:
    #         game_is_on = False
    #         pass
    #     else:
    #         pass


    if player.ycor() >= 250:
        scoreboard.level_up()
        player.teleport(0, -280)
        car.level_up()
        # player = Player()
        # car_list = []
        # car = CarManager()
        # scoreboard = Scoreboard()
        # car_list.append(car)
        # screen.clear()

if not game_is_on:
    screen.clearscreen()
    scoreboard.game_over()

screen.exitonclick()

