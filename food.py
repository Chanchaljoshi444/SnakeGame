from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()    #optional
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)

    def refresh(self):
        self.ht()
        self.penup()
        self.goto(x=randint(-280, 280), y=randint(-280, 270))  #270 so that the food doesnt land overlapping the score
        self.st()

#this is good but lets implement the Food class using inheritance
# class Food():
#     def __init__(self, color = "red", shape = "circle"):
#         self.color = color
#         self.shape = shape
#         self.food = Turtle(self.shape)
#
#     def create_food(self):
#         self.food.color(self.color)
#         self.food.ht()
#         self.food.penup()
#         self.food.goto(x=randint(-270, 270), y=randint(-270, 270))
#         self.food.st()