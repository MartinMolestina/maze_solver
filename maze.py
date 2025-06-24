from window import Cell, Window
import time, random

class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        

        if seed is not None:
            random.seed(seed)

        self.__cells = []

        self.__create_cells()

        self.__break_entrance_and_exit()

        self.__break_walls_r(0, 0)  # Start maze generation from top-left

        self.__reset_cells_visited()



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

        if self.__win is not None:
            # Animate the drawing
            self.__animate()

    def __animate(self):
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        # Entrance: top-left cell
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        # Exit: bottom-right cell
        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1
        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)

    def __break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True

        # Define possible directions: (name, dx, dy)
        directions = [
            ("left",  -1,  0),
            ("right",  1,  0),
            ("up",     0, -1),
            ("down",   0,  1),
        ]

        random.shuffle(directions)  # Shuffle to make paths different each time

        for direction, dx, dy in directions:
            ni = i + dx
            nj = j + dy

            # Skip out-of-bounds
            if ni < 0 or ni >= self.__num_cols or nj < 0 or nj >= self.__num_rows:
                continue

            neighbor = self.__cells[ni][nj]

            if not neighbor.visited:
                # Break walls between current and neighbor
                if direction == "left":
                    current.has_left_wall = False
                    neighbor.has_right_wall = False
                elif direction == "right":
                    current.has_right_wall = False
                    neighbor.has_left_wall = False
                elif direction == "up":
                    current.has_top_wall = False
                    neighbor.has_bottom_wall = False
                elif direction == "down":
                    current.has_bottom_wall = False
                    neighbor.has_top_wall = False

                # Redraw both cells if window is available
                self.__draw_cell(i, j)
                self.__draw_cell(ni, nj)

                # Recursive call
                self.__break_walls_r(ni, nj)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False


    def solve(self):
        return self.__solve_r(0, 0)


    def __solve_r(self, i, j):
        self.__animate()  # Step 1: animate traversal
        current = self.__cells[i][j]
        current.visited = True  # Step 2: mark visited

        # Step 3: check if we're at the goal
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # Step 4: explore each direction
        directions = [
            ("left",  -1,  0, "has_left_wall", "has_right_wall"),
            ("right",  1,  0, "has_right_wall", "has_left_wall"),
            ("up",     0, -1, "has_top_wall", "has_bottom_wall"),
            ("down",   0,  1, "has_bottom_wall", "has_top_wall"),
        ]

        for direction, dx, dy, wall_attr, neighbor_wall_attr in directions:
            ni = i + dx
            nj = j + dy

            # Bounds check
            if ni < 0 or ni >= self.__num_cols or nj < 0 or nj >= self.__num_rows:
                continue

            neighbor = self.__cells[ni][nj]

            # If there's no wall in the way and neighbor isn't visited
            if not getattr(current, wall_attr) and not neighbor.visited:
                current.draw_move( neighbor)  # Step 5a: draw move

                if self.__solve_r(ni, nj):           # Step 5b: recurse
                    return True

                current.draw_move(neighbor, undo=True)  # Step 5c: draw undo

        # Step 6: no valid moves, dead end
        return False


