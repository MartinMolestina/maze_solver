# 🧩 Maze Generator & Solver in Python

A graphical maze generator and solver implemented in Python using `tkinter`.  
This project uses recursive algorithms for both maze generation and solving, and provides a step-by-step animation of the process.

---

## 🎯 Features

- ✅ Random maze generation using depth-first search (DFS)
- ✅ Optional random seed for reproducibility
- ✅ Visual animation using `tkinter`
- ✅ Maze solving with a second DFS traversal
- ✅ Backtracking path shown in gray, solution path in red
- ✅ Unit tests for core logic (cell creation, visited reset, etc.)

---

## 🧠 Algorithms Used

### Maze Generation

- Uses recursive **backtracking (DFS)**.
- Cells are visited one-by-one in a shuffled order, and walls are removed between visited neighbors.
- Animated with slight delay to visualize the process.

### Maze Solving

- Uses another **recursive DFS**.
- Tracks visited cells and draws:
  - **Red lines** for correct path.
  - **Gray lines** for backtracking.

---

## 🛠️ How It Works

- A `Maze` is made of a 2D grid of `Cell` objects.
- Each `Cell` tracks its wall state (top, bottom, left, right).
- A `Window` class wraps a `tkinter.Canvas` for drawing lines and cells.
- Movement between cells is visualized by drawing lines from cell center to center.

---

## ▶️ How to Run

### Requirements

- Python 3.10+
- No extra packages required (only standard library)
- Tested on:
  - ✅ Arch Linux + Hyprland


### Run it

```bash
python3 main.py
