import matplotlib.pyplot as plt


class Chessboard:
    def __init__(self, size=8):
        self.size = size
        self.board = [[(i + j) % 2 for i in range(size)] for j in range(size)]
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticks(range(self.size))
        self.ax.set_yticks(range(self.size))
        self.ax.set_xticklabels(range(1, self.size + 1))
        self.ax.set_yticklabels(range(1, self.size + 1))
        self.ax.set_aspect('equal')
        self.im = self.ax.imshow(self.board, cmap='Oranges', origin='lower')
        self.queens = []
        self.highlight = None
        self.finished = False
        self.current_frame = 0
        self.num_actions = 0

    def placeQueen(self, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("Posição inválida.")
            return
        queen = self.ax.plot(x, y, marker='o', markersize=20, color='grey')[0]
        self.queens.append(queen)

    def checkPosition(self, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("Posição inválida.")
            return
        if self.highlight:
            self.highlight.remove()
        self.highlight = self.ax.plot(
            x, y, marker='^', markersize=10, color='blue')[0]

    def update(self, action):
        x, y, action_type = action
        if action_type == 'place':
            self.placeQueen(x, y)
        elif action_type == 'check':
            self.checkPosition(x, y)
        self.current_frame += 1
        if self.current_frame >= self.num_actions:
            self.finished = True

    def animate(self, action):
        self.update(action)
        if self.finished:
            self.highlight.remove()
            plt.show()  # Manter o gráfico estático no último quadro
        else:
            self.fig.canvas.flush_events()
            plt.pause(0.5)


# Test the class
chessboard = Chessboard()
actions = [
    (0, 0, 'place'),
    (1, 1, 'check'),
    (2, 2, 'place'),
    (3, 3, 'check'),
    (4, 4, 'place'),
    (5, 5, 'check'),
    (6, 6, 'place'),
    (7, 7, 'check'),
    (3, 3, 'place'),
    (5, 5, 'check'),
    (0, 0, 'place'),
]

chessboard.num_actions = len(actions)

for action in actions:
    chessboard.animate(action)
