import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("grey")
t.speed(10)
t.pensize(10)
turtle.bgcolor("#FFFFFF")
t.penup()
t.goto(-100,200)
t.pendown()
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.end_fill()
t.color("black")
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.penup()
t.goto(50,100)
t.color("white")
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()
t.penup()
t.goto(50,-100)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(50)
t.end_fill()



while True :
    time_light = turtle.numinput("trafficlight","predict color of the trafic light in minutes ",minval=1,maxval=60)
    if time_light > 0 and time_light <= 3 :

        t.color("green")
        t.penup()
        t.goto(50,-100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.color("white")
        t.penup()
        t.goto(50,100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
    elif time_light >=4 and time_light <=5 :
        t.color("red")
        t.penup()
        t.goto(50,100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.color("white")
        t.penup()
        t.goto(50,-100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
    elif time_light >=6 and time_light <=9 :
        t.color("green")
        t.penup()
        t.goto(50,-100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.color("white")
        t.penup()
        t.goto(50,100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()

    elif time_light >=10 and time_light <= 11 :
        t.color("red")
        t.penup()
        t.goto(50,100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.color("white")
        t.penup()
        t.goto(50,-100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()

    elif time_light >=12 and time_light <=15 :
        t.color("green")
        t.penup()
        t.goto(50,-100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        t.color("white")
        t.penup()
        t.goto(50,100)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()












































































turtle.exitonclick()