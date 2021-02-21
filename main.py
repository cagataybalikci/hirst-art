# import  colorgram as cg
#
# extracted_colors = cg.extract("hirst_image.jpg", 10)
# color_palette = []
# for color in extracted_colors:
#     r_color =color.rgb.r
#     g_color = color.rgb.g
#     b_color = color.rgb.b
#     new_color = (r_color, g_color, b_color)
#     color_palette.append(new_color)

# With the code above while using cologram package,
# colors in hirst_image extracted and added to color_palette.
# Rest of the code commented to reduce to run time. And the values are copy-pasted on list item.

from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
screen.title("Hirst Art")
t.shape("circle")
t.penup()
t.speed("fast")
screen_width = screen.window_width()
screen_height = screen.window_height()
color_palette = [(246, 245, 243), (234, 240, 246), (240, 246, 243), (247, 239, 243), (131, 165, 206),
                 (225, 151, 100), (32, 41, 59), (200, 134, 147), (235, 212, 87), (166, 56, 46)]


def get_random_color():
    t.color((random.choice(color_palette)))


def draw_circle(x_pos, y_pos):
    for column in range(1, 11):
        t.setposition(-x_pos / 2, (-y_pos / 2) + (column * 50))
        for row in range(1, 11):
            get_random_color()
            t.forward(50)
            t.stamp()


draw_circle(screen_width, screen_height)
screen.exitonclick()
