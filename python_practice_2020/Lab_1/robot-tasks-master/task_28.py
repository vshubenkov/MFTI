#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    index = 0
    while index < 5:
        move_right()
        if cell_is_filled():
            index += 1



if __name__ == '__main__':
    run_tasks()
