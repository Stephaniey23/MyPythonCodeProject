"""
File: CheckerboardKarel.py
Name: Stephanie
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is on the left end most of the bottom of the world, facing East
    post-condition: Karel is on the left most end of the top street of the pillar, facing East
    """

    if front_is_clear():
        do_line()
        # while front_is_clear():
        #     checkerboard_one_row()
        #     go_back()
        #     turn_around()
        #     go_to_next()
        #     fill_in_next_line()
        #     go_back()
        #     turn_around()
        #     go_to_next()
    else:
        turn_left()
        do_line()


def do_line():
    while front_is_clear():
        checkerboard_one_row()
        go_back()
        turn_around()
        go_to_next()
        fill_in_next_line()
        go_back()
        turn_around()
        go_to_next()


def checkerboard_one_row():
    """
    pre-condition: Karel is on the left most end of line 1, facing East
    post-condition: Karel is on the right most end of line 1, facing East
    """
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
        else:
            pass
    put_beeper()
    turn_around()
    move()
    if not on_beeper():
        move_back()
    else:
        move_back()
        pick_beeper()


def move_back():
    turn_left()
    turn_left()
    move()


def go_back():
    turn_left()
    turn_left()
    while front_is_clear():
        move()


def turn_around():
    turn_right()
    turn_right()


def go_to_next():
    turn_left()
    if front_is_clear():
        move()
        turn_right()


def fill_in_next_line():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
