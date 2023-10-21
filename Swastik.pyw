import turtle

a = turtle.Turtle()
a.color("orange")
a.begin_fill()
a.turtlesize(1)

a.speed(1.3)


for i in range(1,5):
    a.left(90)
    a.forward(100)
    a.right(90)
    a.forward(110)
    a.left(50)
    a.forward(30)
    a.right(150)
    a.forward(20)
    a.right(30)
    a.forward(20)
    a.right(50)
    a.forward(100)
    a.left(90)
    a.forward(88)


a.end_fill()
a.hideturtle()
turtle.done()
