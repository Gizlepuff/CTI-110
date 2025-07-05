#Jonas Hall
#7/5/25
#P4LAB1
#Draws a suare and a triangle
import turtle

t = turtle.Turtle()
t.speed(2)

i = 0
while i < 4:
    t.forward(100)
    t.right(90)
    i += 1

t.penup()
t.goto(150, 0)
t.pendown()

j = 0
while j < 3:
    t.forward(100)
    t.right(120)
    j += 1

turtle.done()
