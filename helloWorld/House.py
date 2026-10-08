# Picture with (Grass, Sky, House, Tree, and Sun ) !!!

import turtle

t=turtle.Turtle()
t.shape("turtle")
t.speed(10)

# Grass !
t.color("#0B8B2E")
t.begin_fill()
t.forward(1000)
t.right(90)
t.forward(500)
t.right(90)
t.forward(2000)
t.right(90)
t.forward(500)
t.right(90)
t.forward(1000)
t.end_fill()


# Sky !
t.color("#99F4FF")
t.begin_fill()
t.forward(1000)
t.left(90)
t.forward(500)
t.left(90)
t.forward(2000)
t.left(90)
t.forward(500)
t.left(90)
t.forward(1000)
t.end_fill()
t.color("#0B8B2E")
t.left(90)
t.forward(150)

# House ! (Wall) Red: #E52B3C    Brown:#8F6800      Blue/Teel: #0D8D94
t.color("#8F6800") 
t.begin_fill()
t.left(180)
t.forward(350)
t.right(90)
t.forward(350)
t.right(90)
t.forward(350)
t.right(90)
t.forward(350)
t.end_fill()


# House ! (Roof)
t.color("#E52B3C")
t.begin_fill()
t.left(120)
t.forward(350)
t.left(120)
t.forward(350)
t.end_fill()


# House ! (Window)
t.color("#8F6800")
t.left(120)
t.forward(100)
t.right(90)
t.forward(200)
t.color("#0D8D94")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()


# Tree ! (Stem) !!! Colors are" Black = #000000  Green =  #1A3A1A
t.color("#8F6800")
t.left(90)
t.forward(250)
t.color("#0B8B2E")
t.forward(200)
t.color("#000000")
t.begin_fill()
t.left(90)
t.forward(250)
t.right(90)
t.forward(30)
t.right(90)
t.forward(250)
t.right(90)
t.forward(30)
t.end_fill()

#Tree (Leaves)   Black = #000000  Green =  #1A3A1A
t.color("#000000")
t.right(90)
t.forward(200)
t.right(90)
t.forward(15)
t.color("#1A3A1A")
t.begin_fill()
# Leaf 1
t.circle(50)
t.end_fill()
t.color("#99F4FF")
t.forward(100)
t.left(90)
t.forward(100)
t.color("#1A3A1A")
t.begin_fill()
# Leaf 2
t.circle(50)
t.end_fill()
t.color("#99F4FF")
t.penup()
t.left(90)
t.forward(100)
t.pendown
t.color("#1A3A1A")
t.begin_fill()
t.right(90)
# Leaf 3
t.circle(50)
t.end_fill()
t.penup()
t.left(90)
t.forward(50)
t.pendown()
t.begin_fill()
# Leaf 4
t.circle(50)
t.penup()
t.end_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
print(t.heading())
t.begin_fill()
t.pendown()
# Leaf 5
t.circle(50)
t.end_fill()
t.pendown()
t.right(90)
t.begin_fill()
t.circle(50)
t.penup() 
t.end_fill()

#Cloud (1) Colors: White:#FFFFFF
t.right(180)
t.forward(250)
t.left(90)
t.forward(100)
t.color("#FFFFFF")
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
t.color("#000000")
t.circle(50)
#Cloud (2)  Colors: White:#FFFFFF
t.right(90)
t.forward(50)
t.color("#FFFFFF")
t.begin_fill()
t.pendown()
t.left(90)
t.circle(50)
t.end_fill()
t.color("#000000")
t.circle(50)
#Cloud (3)
t.right(90)
t.forward(50)
t.color("#FFFFFF")
t.begin_fill()
t.pendown()
t.left(90)
t.circle(50)
t.end_fill()
t.color("#000000")
t.circle(50)
#Clound (4)
t.right(90)
t.forward(50)
t.color("#FFFFFF")
t.begin_fill()
t.pendown()
t.left(90)
t.circle(50)
t.end_fill()
t.color("#000000")
t.circle(50)
t.penup()
t.end_fill()


#Sun And Rays  !!! Colors : #FFD700
t.right(90)
t.forward(300)
t.color("#FFD700")
t.pendown()
t.begin_fill()
t.circle(75)
t.penup()
t.end_fill()
t.pensize(1)
t.right(90)
t.forward(30)
t.right(90)
t.begin_fill()
t.pendown()
t.right(90)
t.forward(10)
t.pensize(5)
t.forward(105)
t.left(90)
t.forward(105)
t.backward(105)
t.left(20)
t.forward(105)
t.backward(105)
t.left(20)
t.forward(105)
t.backward(105)
t.left(20)
t.forward(105)
t.backward(105)


           

















turtle.exitonclick()







