"""
File: CollectNewspaperKarel.py
Name: Stephanie
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *

def main():
    """
    pre-condition: Karel is facing East, on (3,4) and move to newspaper, on (6,3)
    post-condition: Karel collected newspaper, on (6,3), and return home,facing East, on (3,4)
    """
    pass
    move_to_newspaper()
    pick_beeper()
    bring_beeper_home()

def move_to_newspaper():
    """
    pre-condition: Karel is facing East, on (3,4)
    post-condition: Karel is facing East, on (6,3)
    """
    pass
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()

def bring_beeper_home():
    """
    pre-condition: Karel is facing East, on (6,3)
    post-condition: Karel is facing East, on (3,4)
    """
    pass
    for i in range(2):
        turn_right()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
