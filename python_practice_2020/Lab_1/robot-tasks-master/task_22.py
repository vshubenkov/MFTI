#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    index_gor = 0
    index_vert = 0
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        index_gor += 1
    while not wall_is_beneath():
        fill_cell()
        move_down()
        index_vert += 1

    if index_gor == 0 and index_vert == 0:
        fill_cell()
    elif index_gor == 0 and index_vert != 0:
        fill_cell()
    elif index_gor != 0 and index_vert == 0:
        while not wall_is_on_the_left():
            move_left()
    else:
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
            for i in range(1, index_vert):
                fill_cell()
                move_up()
            if wall_is_on_the_left():
                fill_cell()
            if not wall_is_on_the_left():
                fill_cell()
                move_left()
                for i in range(1, index_vert):
                    fill_cell()
                    move_down()
                if wall_is_on_the_left():
                    fill_cell()
            else:
                for i in range(1, index_vert):
                    move_down()






if __name__ == '__main__':
    run_tasks()
