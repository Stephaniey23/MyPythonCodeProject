"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10 # 100 frames per second
NUM_LIVES = 3 # Number of attempts


def main():

    graphics = BreakoutGraphics()
    window = graphics.get_window()
    brick = graphics.get_brick()
    ball = graphics.get_ball()
    paddle = graphics.get_paddle()
    life_label = graphics.get_life_label()
    ball.x1 = ball.x
    ball.y1 = ball.y
    ball_radius = graphics.get_ball()
    r = ball_radius
    life = NUM_LIVES

    # Add the animation loop here!
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()

    # Update
        ball.move(dx, dy)

    # Check
        if ball.y + ball.height >= window.height:
            ball.x = ball.x1
            ball.y = ball.y1
            life = life - 1

        else:
            if ball.x <= 0 or ball.x + ball.width >= window.width:
                graphics.set_dx(-dx)

            if ball.y <= 0:
                graphics.set_dy(-dy)

        # adding the check system to check 4 corners of ball, instead of only checking one corner
        for i in range(2):
            for j in range(2):
                check_x = ball.x + i * ball.width
                check_y = ball.y + j * ball.width
                obj = window.get_object_at(check_x, check_y)

                if obj is not None and obj is not life_label:

                    # adding the check point to tell it's paddle or brick
                    if obj is paddle:
                        if dy > 0:
                            graphics.set_dy(-dy)
                    else:
                        window.remove(obj)
                        graphics.set_dy(-dy)
                else:
                    break

        if life <= 0:
            break

    # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()