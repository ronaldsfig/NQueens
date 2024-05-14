import random
import math
from chessboardAnimation import ChessboardAnimation
from temperatureAnimation import TemperatureAnimation
import matplotlib.pyplot as plt
import copy
import time


class Chessboard:
    def __init__(self, size):
        self.size = size
        self.board = [None] + [0] * size

    def displayChessboard(self):
        for i in range(1, self.size + 1):
            row = ""
            for j in range(1, self.size + 1):
                if self.board[j] == i:
                    row += " O "
                else:
                    row += " - "
            print(row)

    def generateFirstPositions(self):
        for i in range(1, len(self.board)):
            self.board[i] = i
        self.permute()

    def permute(self):
        for i in range(self.size, 1, -1):
            j = random.randint(1, i - 1)
            self.swapPositions(i, j)

    def swapPositions(self, x, y):
        if x < 1 or x > self.size or y < 1 or y > self.size:
            print("Índice inválido.")
            return
        self.board[x], self.board[y] = self.board[y], self.board[x]
        return

    def getRandomPosition(self, target_x, target_y):
        y = random.randint(1, self.size)
        if y == target_y or y == target_x:
            return self.getRandomPosition(target_x, target_y)
        return y

    """
    def fitness(self):
        fit, target_x, target_y = 0, 0, 0
        for i in range(1, self.size+1):
            right_diagonal_a = self.board[i]-i
            left_diagonal_a = self.board[i]+i

            for j in range(i + 1, self.size+1):
                right_diagonal_b = self.board[j]-j
                left_diagonal_b = self.board[j]+j

                if (right_diagonal_a == right_diagonal_b) or (left_diagonal_a == left_diagonal_b):
                    fit += 1
                    target_x, target_y = i, j

        return fit, target_x, target_y
    """

    def fitness(self):
        for i in range(1, self.size+1):
            right_diagonal_a = self.board[i]-i
            left_diagonal_a = self.board[i]+i

            for j in range(i + 1, self.size+1):
                right_diagonal_b = self.board[j]-j
                left_diagonal_b = self.board[j]+j

                if (right_diagonal_a == right_diagonal_b) or (left_diagonal_a == left_diagonal_b):
                    return (self.size * self.size) - (i * j), i, j

        return 0, 0, 0

    def disturbance(self, target_x, target_y):
        random_position = self.getRandomPosition(target_x, target_y)
        self.swapPositions(target_y, random_position)
        return

    def cooling(self, temperature, iteration):
        return (0.99 ** iteration) * temperature

    def simulatedAnnealing(self, temperature):
        self.generateFirstPositions()
        solution = [self.board, self.fitness()]

        iteration = 1
        while solution[1][0] != 0:
            self.disturbance(solution[1][1], solution[1][2])
            new_solution = [self.board, self.fitness()]

            if new_solution[1][0] < solution[1][0]:
                solution = new_solution
            else:
                probability = math.e ** ((solution[1][0] - new_solution[1][0]) / (
                    temperature + 0.000000000000001))

                if (probability - ((random.randint(1, 100))/100) >= 0):
                    solution = new_solution
                else:
                    self.board = solution[0]

            temperature = self.cooling(temperature, iteration)
            iteration += 1

    """
    def simulatedAnnealingVisual(self, temperature):
        board_frames = []
        graphic_frames = []
        self.generateFirstPositions()
        solution = [self.board, self.fitness()]

        iteration = 1
        board_frames.append(copy.deepcopy(self.board))
        graphic_frames.append([0, temperature, solution[1][0]])
        while solution[1][0] != 0:
            self.disturbance(solution[1][1], solution[1][2])
            new_solution = [self.board, self.fitness()]

            if new_solution[1][0] < solution[1][0]:
                solution = new_solution
                board_frames.append(copy.deepcopy(self.board))
                graphic_frames.append(
                    [iteration, temperature, new_solution[1][0]])
            else:
                probability = math.e ** ((solution[1][0] - new_solution[1][0]) / (temperature + 0.000000000000001))

                if (probability - ((random.randint(1, 100))/100) >= 0):
                    print("aqui foi")
                    solution = new_solution
                    board_frames.append(copy.deepcopy(self.board))
                    graphic_frames.append(
                        [iteration, temperature, new_solution[1][0]])
                else:
                    self.board = solution[0]
                    board_frames.append(copy.deepcopy(self.board))
                    graphic_frames.append(
                        [iteration, temperature, solution[1][0]])

            temperature = self.cooling(temperature, iteration)
            iteration += 1

        return board_frames, graphic_frames


size = 6
chessboard = Chessboard(size)
animation = ChessboardAnimation(size)
animation2 = TemperatureAnimation()
animation3 = TemperatureAnimation()

frames = chessboard.simulatedAnnealingVisual(4000)

board_frames = frames[0]
graphic_frames = frames[1]

frame = 0
for board in board_frames:
    queens = [(i - 1, board[i] - 1) for i in range(1, size+1)]
    animation.update_board(queens)

    graphic = graphic_frames[frame]
    animation2.update_graph(graphic[0], graphic[1])
    animation3.update_graph(graphic[0], graphic[2])

    frame += 1

plt.show()
"""


size = 12
chessboard = Chessboard(size)

start = time.time()
chessboard.simulatedAnnealing(4000)
print("Runtime in second:", time.time() - start)

chessboard.displayChessboard()
