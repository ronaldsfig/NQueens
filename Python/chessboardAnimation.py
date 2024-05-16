import matplotlib.pyplot as plt
import numpy as np


class ChessboardAnimation:
    def __init__(self, size):
        self.size = size
        self.fig, self.ax = plt.subplots()
        self.board = np.zeros((size, size))

    def updateBoard(self, queens):
        self.board = np.zeros((self.size, self.size))
        for queen in queens:
            self.board[queen[0]][queen[1]] = 1

        self.ax.clear()
        self.ax.imshow(self.board, cmap='binary', origin='upper')
        self.ax.set_title('Tabuleiro')
        self.ax.set_xticks(np.arange(0.5, self.size, 1))
        self.ax.set_yticks(np.arange(0.5, self.size, 1))
        self.ax.set_xticklabels(np.arange(1, self.size + 1, 1))
        self.ax.set_yticklabels(np.arange(self.size, 0, -1))
        self.ax.grid(color='black', linestyle='-', linewidth=1)
        self.fig.canvas.draw()
        plt.pause(0.01)

    def animate(self, frames):
        for frame in frames:
            queens = [(frame[i], i) for i in range(self.size)]
            self.updateBoard(queens)
