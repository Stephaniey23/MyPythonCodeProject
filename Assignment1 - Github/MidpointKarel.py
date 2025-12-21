"""
File: MidpointKarel.py
Name: Stephanie
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *
from CollectNewspaperKarel import *


def main():
    """
    pre-condition: Karel is facing East, on(1,1)
    post-condition: Karel is in the middle of street1, and put beeper
    """
    fill_left_upper_side()
    turn_back()
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    fill_right_upper_side()
    go_back_to_beginning()
    pick_beeper_on_left_upper_side()
    put_beeper_on_midpoint()
    turn_left()
    while front_is_clear():
        move()
    turn_around()
    pick_beeper_on_right_upper_side()
    go_back_to_beginning()
    while front_is_clear():
        if not on_beeper():
            move()


def fill_left_upper_side():
    while front_is_clear():
        put_beeper()
        move()
        go_to_next()
    put_beeper()


def fill_right_upper_side():
    while front_is_clear():
        put_beeper()
        move()
        turn_right()
        move()
        turn_left()
    put_beeper()


def go_to_next():
    turn_left()
    move()
    turn_right()


def turn_back():
    turn_around()
    while front_is_clear():
        move()
        turn_left()
        move()
        turn_right()


def turn_around():
    turn_left()
    turn_left()


def go_back_to_beginning():
    turn_left()
    while front_is_clear():
        move()
    turn_left()


def pick_beeper_on_left_upper_side():
    while front_is_clear():
        pick_beeper()
        move()
        go_to_next()
    pick_beeper()


def put_beeper_on_midpoint():
    turn_around()
    while front_is_clear():
        if not on_beeper():
            move()
            turn_left()
            if on_beeper():
                pick_beeper()
                while front_is_clear():
                    move()
            else:
                move()
                turn_right()
        else:
            pick_beeper()
            turn_left()
            while front_is_clear():
                move()
    put_beeper()


def pick_beeper_on_right_upper_side():
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
            turn_right()
            move()
            turn_left()
        else:
            move()
            turn_right()
            move()
            turn_left()
    pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
