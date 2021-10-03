from tkinter import *
from random import randrange as rnd, choice
import time
import math

i = 0

class cl_initialization_window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry(str(self.width) + 'x' + str(self.height))
        self.canv = Canvas(self.root, bg='white')
        self.canv.pack(fill=BOTH, expand=1)
        #canv.create_oval(300, 300, 400, 400, fill='red', width=0)
        #canv.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')

class cl_create_ball:
    def __init__(self, window):
        self.window = window
        self.x = rnd(100, window.width - 100)
        self.y = rnd(100, window.height - 100)
        self.r = rnd(30, 50)
        self.dx = +1
        self.dy = +1
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.ball_id = window.canv.create_oval(self.x - self.r, self.y - self.r,
                                             self.x + self.r, self.y + self.r,
                                             fill=choice(self.colors), width=0)
    def move_ball(self, window):
        self.x += self.dx
        self.y += self.dy
        if self.x - self.r <= 0 or self.x + self.r >= window.width:
            self.dx = -self.dx
        elif self.y - self.r <= 0 or self.y + self.r >= window.height:
            self.dy = -self.dy

        f_ball_colision(self)
        window.canv.move(self.ball_id, self.dx, self.dy)
        window.root.after(10, self.move_ball, window)

class cl_create_aim:
    def __init__(self, window):
        self.window = window
        self.x = rnd(100, window.width - 100)
        self.y = rnd(100, window.height - 100)
        self.r = rnd(30, 50)
        self.dx = +1
        self.dy = +1
        self.ball_id = window.canv.create_oval(self.x - self.r, self.y - self.r,
                                               self.x + self.r, self.y + self.r,
                                               fill="lightgrey", outline='white')
    def move_aim(self, window):
        self.x += self.dx
        self.y += self.dy
        if self.x - self.r <= 0 or self.x + self.r >= window.width:
            self.dx = -self.dx
        elif self.y - self.r <= 0 or self.y + self.r >= window.height:
            self.dy = -self.dy

        f_ball_colision(self)
        window.canv.move(self.ball_id, self.dx, self.dy)
        window.root.after(10, self.move_ball, window)

def f_ball_colision(ball):
    for i in ball_list:
        if ball.ball_id != i.ball_id:
            if math.sqrt((ball.x - i.x)**2 + (ball.y - i.y)**2) <= ball.r + i.r:
                ball.dx = -ball.dx
                ball.dy = -ball.dy
    print(ball.ball_id)



window = cl_initialization_window(600, 500)
ball_list = [cl_create_ball(window) for i in range(4)]

ball_list[0].move_ball(window)
ball_list[1].move_ball(window)
ball_list[2].move_ball(window)
ball_list[3].move_ball(window)

#window.canv.bind('<Button-1>', lambda event, f=i: click(event, i))

mainloop()