#Jonas Hall
#7/5/25
#P4LAB1b
#Draws my initials
import turtle


t = turtle.Turtle()
t.color("Red")      
t.pensize(2)          
t.speed(2)


t.penup()
t.goto(-100, 0)      
t.setheading(0)      
t.pendown()
t.forward(50)        
t.backward(25)       
t.right(90)
t.forward(100)       
t.right(90)
t.forward(25)      
t.right(90)
t.forward(20)
t.penup()
t.goto(50, 0)         
t.setheading(270)     
t.pendown()
t.forward(100)       
t.penup()
t.backward(50)       
t.setheading(0)      
t.pendown()
t.forward(50)        
t.setheading(270)    
t.penup()
t.goto(100, 0)      
t.pendown()
t.forward(100)
t.hideturtle()
turtle.done()
