from turtle import Turtle, Screen
import random

win = Screen()
sam = Turtle()
win.bgcolor('black')
sam.penup()
sam.goto(x=200 , y=200)
sam.pendown()


sam.speed('fastest')
def draw ():
    for _ in range(20):
        sam.circle(50)
        sam.color('white')
        sam.left(360 / 20)

def main():
    for _ in range(20):
        sam.color('white')
        sam.forward(50)
        sam.left(120)
        sam.left(10)
    


main()






win.exitonclick()