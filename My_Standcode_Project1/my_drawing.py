"""
File: my_drawing.py
Name: Stephanie
----------------------
TODO: To draw a surprised face
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: draw a surprised face
    """
    window = GWindow(width=700, height=700, title='surprised face')
    face = GOval(500, 600, x=50, y=30)
    face.filled = True
    face.fill_color = 'lightpink'
    window.add(face)
    l_eye = GOval(50, 50, x=100, y=150)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye)
    r_eye = GOval(50, 50, x=300, y=150)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye)
    mouth = GRect(100, 250, x=200, y=300)
    mouth.filled = True
    mouth.fill_color = 'red'
    window.add(mouth)


if __name__ == '__main__':
    main()
