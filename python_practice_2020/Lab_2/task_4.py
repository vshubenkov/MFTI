import turtle
import math

turtle.shape('turtle')

for i in range(15, 110, 10):

    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)

    turtle.right(45)
    turtle.forward(math.sqrt(5**2+5**2))
    turtle.left(135)





