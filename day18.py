""" Advent of Code 2015 day 18 """

import numpy as np
from scipy.ndimage import convolve

INPUT_FILE = "input18.txt"
NUMBER_OF_STEPS = 100


class Board:
    def __init__(self, filename, part=1):
        self.part = part
        self.n = None
        self.m = None
        self.board = None
        self.mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

        self.get_board_from_string(filename)

    def __repr__(self):
        return str(self.board)

    def get_board_from_string(self, filename):
        board = np.loadtxt(filename, dtype=str, comments="//")
        board = np.array([list(row) for row in board])
        board = np.where(board == ".", 0, board)
        board = np.where(board == "#", 1, board)
        self.board = board.astype(int)
        self.broken_lights()
        self.m, self.n = board.shape

    def next_step(self):
        board = np.zeros((self.m, self.n)).astype(int)
        neighbours = convolve(self.board, self.mask, mode="constant", cval=0)
        self.board = np.where(
            np.logical_or(
                neighbours == 3, np.logical_and(neighbours == 2, self.board == 1)
            ),
            1,
            board,
        )
        self.broken_lights()

    def go_n_steps(self, n):
        for _ in range(n):
            self.next_step()

    def get_number_of_lights(self):
        return self.board.sum()

    def broken_lights(self):
        if self.part == 2:
            (
                self.board[0, 0],
                self.board[0, -1],
                self.board[-1, 0],
                self.board[-1, -1],
            ) = (1, 1, 1, 1)


if __name__ == "__main__":
    board = Board(INPUT_FILE)
    board.go_n_steps(NUMBER_OF_STEPS)

    print("Part 1:\t", board.get_number_of_lights())

    board = Board(INPUT_FILE, 2)
    board.go_n_steps(NUMBER_OF_STEPS)
    print("Part 2:\t", board.get_number_of_lights())
