import turtle 
t=turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.color("purple")
t.pensize(10)
t.penup()
t.goto(0,0)
t.pendown()
length = 10
for i in range (25):
    length=length+10
    t.forward(length)
    t.left(30)





turtle.exitonclick()