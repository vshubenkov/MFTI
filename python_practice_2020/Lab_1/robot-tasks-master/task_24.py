#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    for i in range(1,3):
        move_right()
    for i in range(1,4):
        move_down()
        fill_cell()
    move_right()
    move_up()
    fill_cell()
    for i in range(1,3):
        move_left()
        fill_cell()

    move_up()



if __name__ == '__main__':
    run_tasks()
