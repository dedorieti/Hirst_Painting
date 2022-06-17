import colorgram as cg
import turtle as t
import random as rdm

no_colors = 30
colors = cg.extract('hirst-dot-painting.jpg', no_colors)
colors_bench = []

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

tim.shape('turtle')
tim.speed("fast")

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_bench.append((r, g, b))

tim.penup()
tim.setpos(-300, -300)

for i in range(10):
    tim.penup()
    tim.setpos(-300, tim.ycor() + 50*1)
    for _ in range(10):
        tim.dot(20, rdm.choice(colors_bench))
        tim.penup()
        tim.forward(50)

tim.hideturtle()
screen.exitonclick()