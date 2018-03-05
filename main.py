import random
import turtle
wn = turtle.Screen()
dist = 260
turtle.pensize(5)
for x in range(9):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r,g,b)
    for y in range(5):
        turtle.right(144)
        turtle.forward(dist)
    turtle.penup()
    turtle.backward(15)
    turtle.left(90)
    turtle.backward(5)
    turtle.right(90)
    turtle.pendown()
    dist -= 30
turtle.hideturtle()
wn.exitonclick()