#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    index = 1
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    while not wall_is_on_the_right():
        for i in range(index):
            if not wall_is_on_the_right():
                move_right()
        if not wall_is_on_the_right():
            fill_cell()
            move_right()
        index += 1




if __name__ == '__main__':
    run_tasks()
