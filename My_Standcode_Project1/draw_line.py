"""
File: draw_line.py
Name: Stephanie
-------------------------
TODO: to draw lines through mouse-tacking
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
number = 1
hole1_x = None
hole1_y = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_hole)


def create_hole(mouse):
    global number, hole1_x, hole1_y
    hole_number = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
    window.add(hole_number)
    if number % 2 != 0:
        hole1_x = hole_number.x
        hole1_y = hole_number.y
    else:
        line = GLine(hole1_x, hole1_y, hole_number.x, hole_number.y)
        window.add(line)
    window.remove(hole_number)
    number += 1


if __name__ == "__main__":
    main()
