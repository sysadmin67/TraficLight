import turtle
import random

t=turtle.Turtle()
t.shape("turtle")
t.speed(5)



t.goto(0,300)
t.write("Y-Axis",font=("Arial", 12, "normal"))
t.goto(0,0)
t.goto(300,0)
t.write("X-Axis",font=("Arial", 12, "normal"))
t.goto(0,0)
t.goto(-300,0)
t.write("X-Axis",font=("Arial", 12, "normal"))
t.goto(0,0)
t.goto(0,-300)
t.write("Y-Axis",font=("Arial", 12, "normal"))
t.goto(0,0)
t.color("blue")
t.dot(20)
t.write("0,0",font=("Arial", 12, "normal"))
#Quadrant 1
t.goto(150,0)
t.goto(150,150)
t.color("red")
t.dot(20)
t.write(f"{t.pos()}",font=("Arial", 14, "normal"))
t.color("black")
t.goto (0,150)
#Quadrant 2
t.goto(0,0)
t.goto(-150,0)
t.goto(-150,150)
t.color("red")
t.dot(20)
t.write(f"{t.pos()}",font=("Arial", 14, "normal"))
t.goto(0,150)
#Quandrant 3 
t.goto(0,-150)
t.goto(-150,-150)
t.dot(20)
t.write(f"{t.pos()}",font=("Arial", 14, "normal"))
t.goto(-150,0)
#Quadrant 4
t.goto(150,0)
t.goto(150,-150)
t.dot(20)
t.write(f"{t.pos()}",font=("Arial", 14, "normal"))
t.goto(0,-150)
#BackRound 
color=turtle.textinput("NOM", "Name of color:") 
turtle.bgcolor(color)
x=random.randint(-400,400)
y=random.randint(-400,400)
t.penup()
t.goto(x,y)
t.pendown()
t.dot(20)
if x > 0 and y > 0 :
    t.write(f"Quadrant 1 {t.pos()} ",font=(" Arial", 14, " normal"))
if x < 0 and y > 0 :
    t.write(f"Quadrant 2 {t.pos()} ",font=(" Arial", 14, " normal"))
if x < 0 and y < 0 :
    t.write(f"Quadrant 3 {t.pos()} ",font=(" Arial", 14, " normal"))
if x > 0 and y < 0 :
    t.write(f"Quadrant 4 {t.pos()} ",font=(" Arial", 14, " normal"))










turtle.exitonclick()
