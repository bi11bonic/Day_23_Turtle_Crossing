#TODO: Create a turtle player that starts at the bottom of the screen and listen for the "Up"
# keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

#TODO: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen. No cars should be generated in the top and bottom 50px
# of the screen (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs.
# If you get stuck, check the video walkthrough in Step 4.

#TODO: Detect when the turtle player collides with a car and stop the game if this happens.
# If you get stuck, check the video walkthrough in Step 5.

#TODO:Detect when the turtle player has reached the top edge of the screen
# (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the
# starting position and increase the speed of the cars. Hint: think about creating an attribute
# and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video
# walkthrough in Step 6.

#TODO: Create a scoreboard that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing, the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck,
# check the video walkthrough in Step 7.








from turtle import Turtle
import random
COLORS = ["red", "orange", "gold", "green", "blue", "purple", "violet", 'turquoise', 'magenta', 'chartreuse']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # pass
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=.8, stretch_len=1.5)
        # self.speed(1)
        self.teleport(x=210, y=random.randint(-200, 200))
        self.setheading(180)
        self.car_list = []
        self.move_dist = 5
        # self.add_car()

    # def create_car(self):
    #     super().__init__()
    #     self.color(random.choice(COLORS))
    #     self.penup()
    #     self.shape("square")
    #     self.shapesize(stretch_wid=.8, stretch_len=1.5)
    #     self.speed(1)
    #     self.teleport(x=210, y=random.randint(-200, 200))
    #     self.setheading(180)

    def car_move(self):
        self.forward(self.move_dist)

    def add_car(self):
        self.car_list.append(CarManager())

    def level_up(self):
        self.move_dist += MOVE_INCREMENT
        print(self.move_dist)

    def where_am_i(self):
        print(self.position())

    # def new_car(self):
        # self.color(random.choice(COLORS))
        # self.penup()
        # self.shape("square")
        # self.shapesize(stretch_wid=.8, stretch_len=1.5)
        # self.speed(1)
        # self.teleport(x=210, y=random.randint(-200, 200))
        # self.setheading(180)

        # self.car_list.append(CarManager())
        # print(self.car_list)
    pass
