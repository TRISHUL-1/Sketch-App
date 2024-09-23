import turtle
import random
color_list = [(244, 241, 235), (234, 245, 240), (247, 238, 242), (239, 242, 247), (38, 103, 152), (214, 68, 95), (215, 147, 99), (158, 64, 93), (40, 133, 84), (229, 209, 98), (119, 187, 164), (47, 168, 104), (212, 123, 145), (31, 54, 128), (232, 78, 52), (126, 156, 188), (149, 79, 58), (25, 167, 197), (21, 45, 87), (11, 99, 54), (168, 205, 194), (139, 33, 47), (63, 44, 50), (56, 54, 53), (118, 98, 176), (243, 161, 149), (234, 167, 181), (241, 219, 4), (167, 25, 17), (182, 186, 215)]

turtle.colormode(255)
pointer = turtle.Turtle()
pointer.speed(0)
pointer.penup()
pointer.hideturtle()

pointer.setheading(225)
pointer.forward(250)
pointer.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    pointer.dot(20, random.choice(color_list))
    pointer.forward(50)

    if dot_count % 10 == 0:
        pointer.setheading(90)
        pointer.forward(50)
        pointer.setheading(180)
        pointer.forward(500)
        pointer.setheading(0)

screen = turtle.Screen()
screen.exitonclick()