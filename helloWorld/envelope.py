import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("grey")
t.speed(10)
t.pensize(2)
t.penup()
t.goto(-150,150)
t.pendown()
t.begin_fill()
t.forward(152)
t.right(90)
t.forward(110)
t.right(90)
t.forward(152)
t.right(90)
t.forward(110)
t.end_fill()


height=turtle.numinput("windowheight","heightpostcard",minval=10,maxval=500)
width=turtle.numinput("windowidth","widthpostcard",minval=10,maxval=500)
t.penup()
t.color("blue")
t.backward(200)
t.pendown()
t.forward(height)
t.right(90)
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
if width<=150 and height <=110 :
    t.color('blue')
    t.write("You'r postcard can fit in the envelop",font=("Arial","14"))
elif width>150 and height>110:
    t.color("red")
    t.write("You'r postcard can not fit into the envelop",font=("Arial","14"))
elif width>150 or height<110:
    t.color("red")
    t.write("You'r postcard can not fit into the envelop",font=("Arial","14"))
elif width<150 or height>110 :
    t.color('red')
    t.write("You'r postcard cant fit in the envelop",font=("Arial","14"))











































turtle.exitonclick()






         























