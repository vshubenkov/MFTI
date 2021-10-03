#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():

    paint_cross()
    for index in range(1,4):
        for i in range(9):
            for i in range(4):
                move_right()
            paint_cross()


        if index == 3:
            for i in range(36):
                move_left()
        else:
            for i in range(4):
                move_down()
            paint_cross()
            for i in range(9):
                for i in range(4):
                    move_left()
                paint_cross()
            for i in range(4):
                move_down()
            paint_cross()

def paint_cross():
    move_right()
    fill_cell()
    move_right()
    move_down()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()
