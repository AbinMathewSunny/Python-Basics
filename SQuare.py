from turtle import Turtle
t=Turtle()
t.up()
t.goto(50,100)
t.down()
t.speed(1)
t.color("blue")
t.fillcolor("blue")
t.width(10)
t.hideturtle()
t.begin_fill()
for count in range(4):
    t.forward(50)
    t.left(90)

t.end_fill()
t.screen.exitonclick()  