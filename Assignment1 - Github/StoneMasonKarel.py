"""
File: StoneMasonKarel.py
Name: Stephanie
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1), facing East
    post-condition: Karel is on the right most end of 1st street of the world, facing East
    """
    pass
    while front_is_clear():
        fix_pillar()
        go_to_next_pillar()
    fix_pillar()
    turn_around()
    move_to_the_end()


def fix_pillar():
    """
    pre-condition: Karel is facing East, on the bottom of the pillar
    post-condition: Karel is facing North, on the top of the pillar
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def go_to_next_pillar():
    """
    pre-condition: Karel is facing North, on the top of the pillar
    post-condition: Karel is facing East, on the bottom of the pillar
    """
    turn_around()
    move_to_the_end()
    go_to_next()


def turn_around():
    for i in range(2):
        turn_left()


def move_to_the_end():
    for i in range(4):
        move()
    turn_left()


def go_to_next():
    if front_is_clear():
        for i in range(4):
            move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
