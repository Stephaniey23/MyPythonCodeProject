"""
File: babygraphics.py
Name: Stephanie
--------------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, this function returns the x coordinate
    of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 計算左右邊界扣除後, 實際可以畫圖的總寬度
    total_space = width - 2 * GRAPH_MARGIN_SIZE

    # 計算每一個年份可以分到多少寬度(欄寬); 須等距分布
    column = total_space / len(YEARS)

    # 計算並回傳目前的x座標: 起點(GRAPH_MARGIN_SIZE)+(*第幾欄)
    return GRAPH_MARGIN_SIZE + column * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # 頂部邊界線:
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # 底部邊界線:
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # 垂直年份線, 與年份文字:
    for i in range(len(YEARS)):
        # 用函式算出 x 座標
        x = get_x_coordinate(CANVAS_WIDTH, i)

        # 畫垂直線:從頂部邊界連到底部邊界
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)

        # 在直線右邊(x+TEXT_DX)加上年份text, 中心點:西北角
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # check要查詢的名字
    for i in range(len(lookup_names)):
        name = lookup_names[i]

        # 使用取餘數來循環選擇顏色
        color_index = i % len(COLORS)
        color = COLORS[color_index]

        # check年份
        for j in range(len(YEARS) - 1):
            # 準備今年(j)的資料為起始點
            year_current = YEARS[j]
            str_year_current = str(year_current)  # 轉字串才能進行資料庫查詢

            # 取得rank
            if str_year_current in name_data[name]:
                rank_current = int(name_data[name][str_year_current])
            else:
                rank_current = MAX_RANK + 1

            # y座標: 先算出可以畫圖的總高度
            draw_height = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE

            if rank_current > MAX_RANK:
                # 1000名以外就在底部
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                label_text = name + " *"
            else:
                # 1000名以內：代入公式
                y1 = GRAPH_MARGIN_SIZE + (rank_current / MAX_RANK) * draw_height
                label_text = name + " " + str(rank_current)

            # x座標
            x1 = get_x_coordinate(CANVAS_WIDTH, j)

            # 準備次一年(j+1)的資料, 以與今年的點進行連線
            year_next = YEARS[j + 1]
            str_year_next = str(year_next)

            # 取得次一年排名
            if str_year_next in name_data[name]:
                rank_next = int(name_data[name][str_year_next])
            else:
                rank_next = MAX_RANK + 1

            # 次一年y座標
            if rank_next > MAX_RANK:
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y2 = GRAPH_MARGIN_SIZE + (rank_next / MAX_RANK) * draw_height

            # 次一年x座標
            x2 = get_x_coordinate(CANVAS_WIDTH, j + 1)

            # 畫連線(從今年連到次一年)
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

            # 加上文字
            canvas.create_text(x1 + TEXT_DX, y1, text=label_text, anchor=tkinter.SW, fill=color)

            # 補上最後一年的文字

        if rank_next > MAX_RANK:
            last_label = name + " *"
        else:
            last_label = name + " " + str(rank_next)

        canvas.create_text(x2 + TEXT_DX, y2, text=last_label, anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
