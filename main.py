from window import Window, Line, Point, Cell

def main():
    win = Window(600, 200)

    cell_width = 100
    cell_height = 100

    # Create and draw 3 cells
    cell1 = Cell(win)
    cell1.draw(0, 0, cell_width, cell_height)

    cell2 = Cell(win)
    cell2.draw(cell_width, 0, 2 * cell_width, cell_height)

    cell3 = Cell(win)
    cell3.draw(2 * cell_width, 0, 3 * cell_width, cell_height)

    # Test draw_move: forward moves in red
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)

    # Test draw_move: undo/backtrack in gray
    cell3.draw_move(cell2, undo=True)

    # Keep window open
    win.wait_for_close()

if __name__ == "__main__":
    main()
