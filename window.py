from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):

        self.root = Tk()
        self.root.title("Maze Generator")

        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(expand=True, fill=BOTH)

        self.running = False
        self.root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line, color):
        line.draw(self.canvas, color)



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, color):
        canvas.create_line(
                self.p1.x, self.p1.y,
                self.p2.x, self.p2.y,
                fill=color,
                width=2)


class Cell:

    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return

        walls = [
            (self.has_top_wall,    Point(x1, y1), Point(x2, y1)),
            (self.has_right_wall,  Point(x2, y1), Point(x2, y2)),
            (self.has_bottom_wall, Point(x2, y2), Point(x1, y2)),
            (self.has_left_wall,   Point(x1, y2), Point(x1, y1)),
        ]

        for has_wall, start, end in walls:
            if has_wall:
                self.__win.draw_line(Line(start, end), "black")


    def draw_move(self, to_cell, undo=False):
        # Set color based on whether it's a move or an undo
        color = "gray" if undo else "red"

        # Start and end points: center of each cell
        x1 = (self.__x1 + self.__x2) // 2
        y1 = (self.__y1 + self.__y2) // 2
        x2 = (to_cell.__x1 + to_cell.__x2) // 2
        y2 = (to_cell.__y1 + to_cell.__y2) // 2

        if self.__win is None:
            return

        # Draw the move
        line = Line(Point(x1, y1), Point(x2, y2))
        self.__win.draw_line(line, color)

