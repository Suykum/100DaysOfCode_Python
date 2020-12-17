from turtle import Turtle, Screen
import random

timmy = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_hexagon():
    timmy.shape("classic")
    num_sides = 2
    while num_sides <= 8:
        timmy.color(random.choice(colours))
        for _ in range(num_sides):
            angle = 360 / num_sides
            timmy.forward(100)
            timmy.right(angle)
        num_sides += 1


def draw_random_walk():
    directions = [0, 90, 180, 270]
    timmy.pensize(10)
    timmy.speed("fastest")
    for _ in range(200):
        timmy.forward(30)
        timmy.color(random.choice(colours))
        timmy.setheading(random.choice(directions))


def spiriograph(size_of_gap):
    timmy.speed("fastest")
    for n in range(int(360 / size_of_gap)):
        timmy.color(random.choice(colours))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


spiriograph(20)

screen = Screen()
screen.exitonclick()