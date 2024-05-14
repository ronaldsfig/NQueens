import matplotlib.pyplot as plt
import numpy as np


class ChessboardAnimation:
    def __init__(self, size):
        self.size = size
        self.fig, self.ax = plt.subplots()
        self.board = np.zeros((size, size))

    def update_board(self, queens):
        self.board = np.zeros((self.size, self.size))
        for queen in queens:
            self.board[queen[0]][queen[1]] = 1

        self.ax.clear()
        self.ax.imshow(self.board, cmap='binary', origin='upper')
        self.ax.set_title('Tabuleiro')
        self.ax.set_xticks(np.arange(-0.5, self.size, 1))
        self.ax.set_yticks(np.arange(-0.5, self.size, 1))
        self.ax.grid(color='black', linestyle='-', linewidth=1)
        self.fig.canvas.draw()
        plt.pause(0.5)  # Ajuste o valor do tempo de pausa conforme necessário

    def animate(self, frames):
        for frame in frames:
            queens = [(frame[i], i) for i in range(self.size)]
            self.update_board(queens)


def main():
    size = 8  # Tamanho do tabuleiro
    frames = [
        [0, 1, 2, 3, 4, 5, 6, 7],  # Frame 1
        [7, 6, 5, 4, 3, 2, 1, 0],  # Frame 2
        [0, 2, 4, 6, 1, 3, 5, 7]   # Frame 3 (exemplo aleatório)
    ]

    animation = ChessboardAnimation(size)
    for frame in frames:
        queens = [(frame[i], i) for i in range(size)]
        animation.update_board(queens)

    plt.show()


if __name__ == "__main__":
    main()