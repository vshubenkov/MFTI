import turtle
import math

turtle.shape('turtle')

temp_rad, temp_gr = 0, 0
i = 1
index = 0

#шаг спирали 1
a = 30
#Первая координата угол в радианах
rad = 0.5

dl = a / (2 * math.pi) * (rad - temp_rad) * math.sqrt(1 + rad**2)

while i < 10000:
    x = rad * 180 / math.pi #Радианы в градусы
    r = a / (2 * math.pi) * (rad / (2 * math.pi)) #Defince Radius
    dl_2 = a / (2 * math.pi) * (rad - temp_rad) * math.sqrt(1 + rad**2)
    turtle.left(x - temp_gr)
    turtle.forward(r)
    print(x - temp_gr, r, dl_2)
    temp_gr = x
    temp_rad = rad
    rad += 1
    i += 1




