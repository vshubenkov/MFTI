import math
import turtle

turtle.shape('turtle')
turtle.left(90)

def n_figure(n, Radius, direction):
    alfa = 360 / n
    a = math.fabs(2 * math.sin(math.pi/n) * Radius)

    if direction == 'left':
        for i in range(n):
            turtle.left(alfa)
            turtle.forward(a)
    elif direction == 'right':
        for i in range(n):
            turtle.right(alfa)
            turtle.forward(a)

angel = [0, 60, 60]

for i in range(5, 50, 5):
    n_figure(50, 35 + i, 'left')
    n_figure(50, 35 + i, 'right')

input()





