import math
import turtle

turtle.shape('turtle')

def n_figure(n, Radius):
    alfa = 360 / n
    a = math.fabs(2 * math.sin(math.pi/n) * Radius)

    angle = (180 - alfa) / 2

    turtle.left(angle)

    for i in range(n):
        turtle.left(alfa)
        turtle.forward(a)

    turtle.right(angle)
    turtle.forward(15)

n = 30

for i in range(3, 20):
    n_figure(i, n)
    n += 15





