from window import Window, Line, Point, Cell
from maze import Maze


def main():
    win = Window(800, 600)

    # Create a maze: (x1, y1, rows, cols, cell_w, cell_h, window, seed)
    maze = Maze(10, 10, 10, 10, 50, 50, win=win, seed=42)

    # Solve the maze and watch the path animate
    maze.solve()

    # Keep the window open until manually closed
    win.wait_for_close()

if __name__ == "__main__":
    main()

