#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    index = 1
    while not wall_is_on_the_right():
        move_right()
        index += 1
    for i in range(index-1):
        move_left()

#    paint_gorizont_above(index, 0, False)
    paint_gorizont_above(index)
    paint_vert_left(index)
    paint_gorizont_down(index)
    paint_vert_right(index)


def paint_gorizont_above(index):

    priznak_1 = True
    priznak_2 = True

    index_in_func = (index - 1) // 2

    while index_in_func > 1:
        move_right()
        fill_cell()
        for i in range(1, index_in_func):
            move_down()
            move_right()
            fill_cell()
        for i in range(1, index_in_func):
            move_up()
            move_right()
            fill_cell()

        index_in_func -= 1

        if index_in_func == 1 and priznak_1:
            move_left()
            fill_cell()
            priznak_1 = False
            for i in range(1, ((index - 1) // 2) + 1):
                move_right()
        else:
            move_left()
            fill_cell()
            for i in range(1, index_in_func):
                move_down()
                move_left()
                fill_cell()
            for i in range(1, index_in_func):
                move_up()
                move_left()
                fill_cell()
            index_in_func -= 1

            if index_in_func == 1 and priznak_2:
                move_right()
                fill_cell()
                priznak_2 = False
                for i in range(1, ((index - 1) // 2) + 1):
                    move_right()

'''
def paint_gorizont_above(index, rec_ini, rec_par):
    if not rec_ini:
        trungle = index - 2
        move_right()
        fill_cell()
        paint_gorizont_above(trungle, True, '')

    if rec_par == 'left':
        pass
    elif rec_par == 'right':
        if index == 1:
            move_left()
            fill_cell()
        else:
            pass
    elif index > 1:
        par_temp = (index - 1) // 2
        while par_temp > 0:
            move_down()
            move_right()
            fill_cell()
            par_temp -= 1
        par_temp = (index - 1) // 2
        while par_temp > 0:
            move_up()
            move_right()
            fill_cell()
            par_temp -= 1
        paint_gorizont_above((index - 1) // 2, True, 'right')
    else:
        pass
'''





def paint_vert_left(index):

    priznak_1 = True
    priznak_2 = True

    index_in_func = (index - 1) // 2

    while index_in_func > 1:
        move_down()
        fill_cell()
        for i in range(1, index_in_func):
            move_left()
            move_down()
            fill_cell()
        for i in range(1, index_in_func):
            move_down()
            move_right()
            fill_cell()

        index_in_func -= 1

        if index_in_func == 1 and priznak_1:
            move_up()
            fill_cell()
            priznak_1 = False
            for i in range(1, ((index - 1) // 2) + 1):
                move_down()
        else:
            move_up()
            fill_cell()
            for i in range(1, index_in_func):
                move_up()
                move_left()
                fill_cell()
            for i in range(1, index_in_func):
                move_up()
                move_right()
                fill_cell()
            index_in_func -= 1
            if index_in_func == 1 and priznak_2:
                move_down()
                fill_cell()
                priznak_2 = False
                for i in range(1, ((index - 1) // 2) + 1):
                    move_down()

def paint_gorizont_down(index):

    priznak_1 = True
    priznak_2 = True

    index_in_func = (index - 1) // 2

    while index_in_func > 1:
        move_left()
        fill_cell()
        for i in range(1, index_in_func):
            move_up()
            move_left()
            fill_cell()
        for i in range(1, index_in_func):
            move_down()
            move_left()
            fill_cell()

        index_in_func -= 1

        if index_in_func == 1 and priznak_1:
            move_right()
            fill_cell()
            priznak_1 = False
            for i in range(1, ((index - 1) // 2) + 1):
                move_left()
        else:
            move_right()
            fill_cell()
            for i in range(1, index_in_func):
                move_up()
                move_right()
                fill_cell()
            for i in range(1, index_in_func):
                move_down()
                move_right()
                fill_cell()
            index_in_func -= 1
            if index_in_func == 1 and priznak_2:
                move_left()
                fill_cell()
                priznak_2 = False
                for i in range(1, ((index - 1) // 2) + 1):
                    move_left()

def paint_vert_right(index):

    priznak_1 = True
    priznak_2 = True

    index_in_func = (index - 1) // 2

    while index_in_func > 1:
        move_up()
        fill_cell()
        for i in range(1, index_in_func):
            move_right()
            move_up()
            fill_cell()
        for i in range(1, index_in_func):
            move_up()
            move_left()
            fill_cell()

        index_in_func -= 1

        if index_in_func == 1 and priznak_1:
            move_down()
            fill_cell()
            priznak_1 = False
            for i in range(1, ((index - 1) // 2) + 1):
                move_down()
        else:
            move_down()
            fill_cell()
            for i in range(1, index_in_func):
                move_down()
                move_right()
                fill_cell()
            for i in range(1, index_in_func):
                move_down()
                move_left()
                fill_cell()
            index_in_func -= 1
            if index_in_func == 1 and priznak_2:
                move_up()
                fill_cell()
                priznak_2 = False
                for i in range(1, ((index - 1) // 2) + 1):
                    move_down()

if __name__ == '__main__':
    run_tasks()
