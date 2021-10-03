#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    #14x14
    index = 12
    move_right()
    move_down()
    while index >= 1:
        for i in range(index):
            fill_cell()
            move_down()
        fill_cell()
        move_right()

        for i in range(index-1):
            fill_cell()
            move_up()
        fill_cell()
        move_right()
        move_down()
        index -= 2

        if index == 0:
            fill_cell()
            move_down()
            for i in range(12):
                move_left()




if __name__ == '__main__':
    run_tasks()
