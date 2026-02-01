"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
X = 0
Y = 0
DX = 0
DY = 0
NUM_LIVES = 3
count = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, x=X, y=Y, dx=DX,
                 dy=DY, life=NUM_LIVES, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=window_width, height=window_height, title=title)

        # Create life label
        self.__life_label = GLabel('NUM of LIFE ==> '+str(life))
        self.__life_label.font = '-15'
        self.__window.add(self.__life_label, x=5, y=self.__life_label.height+8)

        # Create a paddle
        self.__paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                      y=window_height-paddle_offset)
        self.__paddle.filled = True
        self.__window.add(self.__paddle)

        # Center a filled ball in the graphical window
        self.__ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius*2)/2,
                          y=(window_height-ball_radius*2)/2)
        self.__ball.filled = True
        self.__window.add(self.__ball)

        # Draw bricks
        for i in range(brick_rows):
            if i == 0 or i == 1:
                color = 'red'
            elif i == 2 or i == 3:
                color = 'orange'
            elif i == 4 or i == 5:
                color = 'yellow'
            elif i == 6 or i == 7:
                color = 'green'
            elif i == 8 or i == 9:
                color = 'blue'
            for j in range(brick_cols):
                self.__brick = GRect(brick_width, brick_height, x=x, y=y+brick_offset)
                self.__brick.filled = True
                self.__brick.fill_color = color
                self.__window.add(self.__brick)
                x = x+brick_width+brick_spacing
            x = 0
            y = y+brick_height

        # Initialize our mouse listeners
        self.__dx = dx
        self.__dy = dy
        onmousemoved(self.paddle_move)
        self.count = 0
        onmouseclicked(self.ball_move)

    def paddle_move(self, mouse):
        self.__paddle.x = mouse.x - self.__paddle.width/2

    def ball_move(self, mouse):
        if self.count < 2:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = random.randint(0, INITIAL_Y_SPEED)
            self.set_dx(self.__dx)
            self.set_dy(self.__dy)
        self.count += 1

    def remove(self):
        obj = self.__window.get_object_at(self.__ball.x, self.__ball.y)
        self.__window.remove(obj)

    def get_window(self):
        return self.__window

    def get_brick(self):
        return self.__brick

    def get_paddle(self):
        return self.__paddle

    def get_ball(self):
        return self.__ball

    def get_ball_radius(self):
        return self.__ball_radius

    def get_life_label(self):
        return self.__life_label

    # Default initial velocity for the ball

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

