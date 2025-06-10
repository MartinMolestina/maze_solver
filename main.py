from window import Window, Line, Point

def main():
    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(750, 750)
    diagonal_line = Line(p1, p2)

    win.draw_line(diagonal_line, "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()
