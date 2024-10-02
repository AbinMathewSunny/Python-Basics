from turtle import Turtle
t=Turtle()
t.screen.title("Demo")
for count in range(100):
    for c in ('blue','red','green'):
        t.color(c)
        t.forward(count)
        t.right(30)
t.screen.exitonclick()