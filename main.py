from window import Window, Line, Point, Cell

def main():
    win = Window(600, 200)

    # Cell size
    cell_width = 100
    cell_height = 100

    # Cell 1: all walls
    cell1 = Cell(win)
    cell1.draw(0, 0, cell_width, cell_height)

    # Cell 2: remove right wall
    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(cell_width, 0, 2 * cell_width, cell_height)

    # Cell 3: remove bottom wall
    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell3.draw(2 * cell_width, 0, 3 * cell_width, cell_height)

    # Keep the window open
    win.wait_for_close()


if __name__ == "__main__":
    main()
