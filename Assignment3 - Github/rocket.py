"""
File: rocket.py
Name: Stephanie
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    To print the 6 parts (head, belt, upper body, lower body, belt, head)
    of a rocket and combine as a whole
    """
    pass
    make_head()
    make_belt()
    make_upper_body()
    make_lower_body()
    make_belt()
    make_head()


def make_head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def make_belt():
    for i in range(1):
        print('+', end='')
    for i in range(SIZE):
        print('=', end='')
    for i in range(SIZE):
        print('=',end='')
    for i in range(1):
        print('+')

# 這個解法不適合於此使用, for loop能用於identify字元, 但無法作為座標進行創造字元
# def make_belt():
#     for i in range(0,8,7):
#         print('+', end='')
#     for i in range(1,7):
#         print('=', end='')
#     print('')


def make_upper_body():
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range((SIZE-1)-i):
            print('.', end='')
        for j in range(i+1):
            print('/''\\', end='')
        for j in range((SIZE-1)-i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


def make_lower_body():
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\''/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
