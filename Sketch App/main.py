from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def movefd():
    pointer.forward(50)

def movebk():
    pointer.backward(50)

def turnLeft():
    current = pointer.heading()
    current += 10
    pointer.setheading(current)

def turnRight():
    current = pointer.heading()
    current -= 10
    pointer.setheading(current)

def clear():
    pointer.reset()

screen.listen()

screen.onkey(movefd, "w")
screen.onkey(movebk, "s")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight, "d")
screen.onkey(clear, "c")

screen.exitonclick()