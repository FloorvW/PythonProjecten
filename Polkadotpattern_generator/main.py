# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)
t = Turtle()
t.penup()
t.hideturtle()
t.setpos(-150, -150)
color_list = [(223, 233, 228), (40, 94, 151), (183, 42, 74), (228, 207, 97), (211, 154, 85), (181, 169, 29), (140, 88, 58), (116, 177, 210), (203, 73, 123), (214, 128, 174), (232, 67, 46), (92, 101, 189), (146, 32, 62), (44, 166, 118), (50, 55, 95), (16, 155, 82), (117, 45, 34), (119, 217, 210), (33, 185, 197), (221, 174, 191), (127, 194, 176), (214, 204, 34), (176, 187, 216), (46, 52, 71), (156, 207, 219), (227, 176, 167), (41, 77, 81)]
t.backward(200)
t.forward(100)


direction = 0
rows = 0


def color():
    x = random.randint(0, 26)
    a = color_list[x]
    return a

def up():
    global rows
    while rows < 10:
        global direction
        if direction % 2 == 0:
            t.right(90)
        else:
            t.left(90)
        t.forward(50)
        t.dot(20, color())
        if direction % 2 == 0:
            t.right(90)
        else:
            t.left(90)
        line_dots()


def line_dots():
    global direction
    global rows
    direction += 1
    rows += 1
    t.dot(20, color())
    for s in range(0, 9):
        t.forward(50)
        t.dot(20, color())
    up()


line_dots()

screen.exitonclick()