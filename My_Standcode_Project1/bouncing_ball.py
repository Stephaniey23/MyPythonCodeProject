"""
File: bouncing_ball.py
Name: Stephanie
-------------------------
TODO: To simulate the moving path of a bouncing ball
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
number = 0
ball1_x = None
ball1_y = None


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    pass
    ball.filled = True
    window.add(ball)
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global number, ball1_x, ball1_y
    window.add(ball)
    vx = VX
    vy = 0
    if number < 3:
        while True:
            vy += GRAVITY
            ball.move(vx, vy)
            if ball.y + ball.height >= window.height:
                if vy > 0:
                    vy = -(vy*REDUCE)
            if ball.x + ball.width >= window.width:
                ball.x = START_X
                ball.y = START_Y
                break
            pause(DELAY)
    number += 1


if __name__ == "__main__":
    main()
