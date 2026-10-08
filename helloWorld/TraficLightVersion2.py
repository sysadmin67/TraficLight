import turtle
import time
import random
t=turtle.Turtle()
t.shape("turtle")
t.color("grey")
t.speed(10)
t.pensize(10)
turtle.bgcolor("#FFFFFF")
t.goto(-100,300)
t.pendown()
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(600)
t.right(90)
t.forward(200)
t.right(90)
t.forward(600)
t.end_fill()
t.color("black")
t.right(90)
t.forward(200)
t.right(90)
t.forward(600)
t.right(90)
t.forward(200)
t.right(90)
t.forward(600)
t.penup()
t.goto(0,175)
t.pendown()
t.color("white")
t.dot(150)
t.penup()
t.goto(0,0)
t.pendown()
t.dot(150)
t.penup()
t.goto(0,-175)
t.pendown()
t.dot(150)

while True :   
#    time_light = turtle.numinput("trafficlight","predict color of the trafic light in minutes ",minval=1,maxval=60)
    time_light=random.randint(1,7)
    if time_light > 0 and time_light <= 3 :
        t.penup()
        t.goto(0,175)
        t.pendown()
        t.color("green")
        t.dot(150)
        t.penup()
        t.goto(0,0)
        t.color("white")
        t.dot(150)
        t.penup()
        t.goto(0,-175)
        t.pendown()
        t.color("white")
        t.dot(150)
        t.penup()
        time.sleep(180)
    if time_light == 4 :
        t.penup()
        t.goto(0,175)
        t.pendown()
        t.color("white")
        t.dot(150)
        t.penup()
        t.goto(0,0)
        t.color("yellow")
        t.dot(150)
        t.penup()
        t.goto(0,-175)
        t.pendown()
        t.color("white")
        t.dot(150)
        t.penup()
        time.sleep(60)
    if time_light >4 and time_light <= 7 :
        t.penup()
        t.goto(0,175)
        t.pendown()
        t.color("white")
        t.dot(150)
        t.penup()
        t.goto(0,0)
        t.color("white")
        t.dot(150)
        t.penup()
        t.goto(0,-175)
        t.pendown()
        t.color("red")
        t.dot(150)
        t.penup()
        time.sleep(120)















turtle.exitonclick()