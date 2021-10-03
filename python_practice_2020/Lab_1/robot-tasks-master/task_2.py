#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    for i in range(4):
        if i == 2:
            fill_cell()
        move_right()
        if i <= 2:
            move_down()

if __name__ == '__main__':
    run_tasks()
