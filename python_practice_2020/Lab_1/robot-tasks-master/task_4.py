#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
#    for i in range(3):
    if not wall_is_above():
        move_up()
    elif not wall_is_on_the_left():
        move_left()
    elif not wall_is_beneath():
        move_down()
    else:
        move_right()



if __name__ == '__main__':
    run_tasks()
