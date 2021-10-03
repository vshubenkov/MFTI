import math
import turtle

turtle.shape('turtle')

def n_figure(n, Radius, direction, angle):
    alfa = 360 / n
    a = math.fabs(2 * math.sin(math.pi/n) * Radius)

    if direction == 'left':
        turtle.left(angle)
        for i in range(n):
            turtle.left(alfa)
            turtle.forward(a)
    elif direction == 'right':
        for i in range(n):
            turtle.right(alfa)
            turtle.forward(a)

angel = [0, 60, 60]

for i in range(3):
    n_figure(70, 40, 'left', angel[i])
    n_figure(70, 40, 'right', angel)

input()





