from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_backward, "b")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear_screen, "c")



screen.exitonclick()