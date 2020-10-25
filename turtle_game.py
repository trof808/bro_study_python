import turtle
import random

colors = ['red', 'blue', 'green', 'black']

t = turtle.Pen()
t.width(3)

for x in range(100):
    random_number = random.randint(0, 3)
    color = colors[random_number]
    t.pencolor(color)
    t.circle(x * 2)
    t.forward(x * 2)
    t.left(45)