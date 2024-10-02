from turtle import Turtle

t=Turtle()
t.speed(0)
def flower():
 for i in range(5):
    t.circle(190,90)
    t.left(90)
    t.circle(190,90)
    t.left(18)
flower()
t.done()