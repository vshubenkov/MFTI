#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    rec_f()

def rec_f():
    par_1 = True
    while not wall_is_on_the_right() and par_1:
        if wall_is_beneath():
            move_right()
        else:
            move_down()
            par_1 = rec_f()

    while not wall_is_on_the_left() and par_1:
        if wall_is_beneath():
            move_left()
        else:
            move_down()
            par_1 = rec_f()

    if wall_is_on_the_left():
        return False







if __name__ == '__main__':
    run_tasks()
