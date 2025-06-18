from window import Cell, Window
import time

class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []

        self.__create_cells()


    def __create_cells(self):
        for col in range(self.__num_cols):
            column = []
            for row in range(self.__num_rows):
                cell = Cell(self.__win)
                column.append(cell)
            self.__cells.append(column)

        # Now that all cells exist, draw them
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]

        # Calculate canvas coordinates for this cell
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        # Draw the cell
        cell.draw(x1, y1, x2, y2)

        # Animate the drawing
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
