import tkinter as tk
from random import randrange as rnd, choice
import math
import time

'''Константы'''
WIDTH = 800
HIGHT = 600

class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text = self.points, font = '28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

class Ball():
    def __init__(self, x, y):
        self.x = 50
        self.y = 450
        self.delta_x = 20
        self.delta_y = 450
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.x_coord = 20
        self.y_coord = 450
        self.an = 0
        self.speed = 0
        self.direction = ['right', 'up']
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def move(self):
        global balls, target
        if self.y_coord >= 550 and self.speed >= 10 and self.direction[0] == 'right':
            self.speed = self.speed/2
            self.vx = self.speed * math.cos(self.an)
            self.vy = self.speed * math.sin(self.an)
            self.x_coord -= self.vx
            self.y_coord += self.vy
        elif self.x_coord >= 780 and self.speed >= 10 and self.direction[0] == 'right':
            self.speed = self.speed/2
            self.vx = self.speed * math.cos(self.an)
            self.vy = self.speed * math.sin(self.an)
            self.x_coord -= self.vx
            self.y_coord += self.vy
        elif self.speed >= 10 and self.direction[0] == 'right':
            self.x_coord += self.vx
            self.y_coord -= self.vy
        elif self.speed >= 10 and self.direction[0] == 'left':
            self.x_coord -= self.vx
            self.y_coord += self.vy
        else:
            pass

        canv.coords(self.id, self.x_coord - self.r, self.y_coord - self.r,
                    self.x_coord + self.r, self.y_coord + self.r)

        if target.live == 0:
            balls.clear()
        elif len(balls) > 3:
            canv.delete(balls.pop(0).id)


    def hittest(self, obj):
        pass
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((obj.x - self.x_coord)**2 + (obj.y - self.y_coord)**2) <= obj.r + self.r:
            return True
        else:
            return False

class Gun():
    def __init__(self, width, hight):
        self.hight = hight
        self.x = 50
        self.y = 450
        self.an = 45
        self.f_on = 0
        self.f1_power = 20
        self.f2_power = 20
        self.id = canv.create_line(self.x, self.y, self.x + self.f1_power * math.cos(math.radians(self.an)),
                                   self.y - self.f1_power * math.sin(math.radians(self.an)), width=7)

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""

        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power/2, self.f1_power) * math.cos(self.an),
                    self.y + max(self.f2_power/2, self.f1_power) * math.sin(self.an))

    def fire_on(self, event):
        self.f_on = 1

    def fire_end(self, event):
        global bullet, balls
        self.f_on = 0
        bullet += 1
        ball = Ball(50, 450)
        ball.r += 5
        self.an = math.atan((event.y-ball.y) / (event.x-ball.x))
        ball.vx = self.f2_power * math.cos(self.an)
        ball.vy = - self.f2_power * math.sin(self.an)
        ball.an = self.an
        ball.speed = self.f2_power
        balls += [ball]
        self.f2_on = 0
        self.f2_power = 20

    def power_up(self):
        if self.f_on:
            if self.f2_power < 200:
                self.f2_power += 5
                print(self.f2_power)
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

def start_game():
    global gun, target, balls, bullet

    canv.bind('<Motion>', gun.targetting)
    canv.bind('<Button-1>', gun.fire_on)
    canv.bind('<ButtonRelease-1>', gun.fire_end)

    target.new_target()

    screen_text = canv.create_text(400, 300, text='', font='28')
    balls = []
    target.live = 1
    bullet = 0
    while target.live or balls:
        for b in balls:
            b.move()
            if b.hittest(target) and target.live:
                target.live = 0
                for b1 in balls:
                    canv.delete(b1.id)
                target.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen_text, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    time.sleep(2)
    canv.itemconfig(screen_text, text='')
    root.after(750, start_game)

root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(WIDTH) + 'x' + str(HIGHT))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

gun = Gun(WIDTH, HIGHT)
target = Target()
#    button = tk.Button(text="start_game", width=15, height=3, command=create_game)
#    button.pack()



bullet = 0
balls = []
start_game()

tk.mainloop()