import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_small_grid(self):
        num_cols = 2
        num_rows = 3
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m2._Maze__cells), num_cols)
        self.assertEqual(len(m2._Maze__cells[0]), num_rows)

    def test_maze_single_cell(self):
        num_cols = 1
        num_rows = 1
        m3 = Maze(0, 0, num_rows, num_cols, 30, 30)
        self.assertEqual(len(m3._Maze__cells), 1)
        self.assertEqual(len(m3._Maze__cells[0]), 1)

    def test_maze_wide_grid(self):
        num_cols = 20
        num_rows = 1
        m4 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m4._Maze__cells), 20)
        self.assertEqual(len(m4._Maze__cells[0]), 1)

    def test_maze_tall_grid(self):
        num_cols = 1
        num_rows = 15
        m5 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m5._Maze__cells), 1)
        self.assertEqual(len(m5._Maze__cells[0]), 15)

    def test_maze_entrance_and_exit(self):
        num_cols = 5
        num_rows = 4
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Call the private method using name mangling
        maze._Maze__break_entrance_and_exit()

        entrance_cell = maze._Maze__cells[0][0]
        exit_cell = maze._Maze__cells[num_cols - 1][num_rows - 1]

        # Check that the top wall is removed at entrance
        self.assertFalse(entrance_cell.has_top_wall)

        # Check that the bottom wall is removed at exit
        self.assertFalse(exit_cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()