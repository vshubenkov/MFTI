#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down()

    paint_cross()

    for i in range(4):
        for i in range(4):
            move_right()
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
