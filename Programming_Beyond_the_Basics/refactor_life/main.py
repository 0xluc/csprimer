import os
import random
import time

DELAY, WIDTH, HEIGHT, ITERATIONS, PROBABILITY = 0.1, 90, 30, 100, 0.3
OFFSETS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def alive(grid, x, y):
    neighbors = sum(grid[(y + dy) % HEIGHT][(x + dx) % WIDTH] for dx, dy in OFFSETS)
    return 2 <= neighbors <= 3 if grid[y][x] else neighbors == 3


if __name__ == "__main__":
    cells = [
        [random.random() < PROBABILITY for _ in range(WIDTH)] for _ in range(HEIGHT)
    ]
    for _ in range(ITERATIONS):
        os.system("clear")  # Windows: os.system('cls')
        print("\n".join("".join("■" if x else "□" for x in row) for row in cells))
        cells = [[alive(cells, x, y) for x in range(WIDTH)] for y in range(HEIGHT)]
        time.sleep(DELAY)
