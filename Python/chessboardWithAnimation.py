from chessboard import Chessboard
from chessboardAnimation import ChessboardAnimation
from graphicAnimation import GraphicAnimation
import matplotlib.pyplot as plt
import random
import math
import copy


class ChessboardWithAnimation(Chessboard):
    def __init__(self, size):
        super().__init__(size)
        self.board_frames = []
        self.graphic_frames = []


    def updateFrames(self, iteration, temperature, fitness):
        self.board_frames.append(copy.deepcopy(self.board))
        self.graphic_frames.append([iteration, temperature, fitness])


    def simulatedAnnealing(self, temperature):
        self.generateFirstPositions()
        solution = [copy.deepcopy(self.board), self.fitness()]

        self.updateFrames(0, temperature, solution[1])
        iteration = 1
        while solution[1] > 0:
            temperature *= (0.99 ** iteration)

            while True:
                queen_x = random.randrange(1, self.size)
                queen_y = random.randrange(1, self.size)

                if queen_x != queen_y:
                    break
            
            self.board[queen_x], self.board[queen_y] = self.board[queen_y], self.board[queen_x]

            new_solution = [copy.deepcopy(self.board), self.fitness()]
            delta = new_solution[1] - solution[1]

            if delta < 0:
                solution = new_solution
                self.updateFrames(iteration, temperature, solution[1])
            else:
                probability = random.uniform(0, 1) < math.exp(-delta / temperature)
                
                if probability:
                    solution = new_solution
                    self.updateFrames(iteration, temperature, solution[1])
                else:
                    self.board = copy.deepcopy(solution[0])
                    self.updateFrames(iteration, temperature, solution[1])

            iteration += 1
        
        return self.board_frames, self.graphic_frames
    

size = 8
chessboard = ChessboardWithAnimation(size)
chessboard_animation = ChessboardAnimation(size)
temperature_animation = GraphicAnimation(
    'Temperatura ao longo do tempo', 'Tempo (t)', 'Temperatura (temp)', 'red')
fitness_animation = GraphicAnimation(
    'Aptidão de soluções', 'Tempo (t)', 'Fitness (fit)', 'blue')

frames = chessboard.simulatedAnnealing(4000)

board_frames = frames[0]
graphic_frames = frames[1]

frame = 0
for board in board_frames:
    queens = [(i - 1, board[i] - 1) for i in range(1, size+1)]
    chessboard_animation.updateBoard(queens)

    graphic = graphic_frames[frame]
    temperature_animation.updateGraphic(graphic[0], graphic[1])
    fitness_animation.updateGraphic(graphic[0], graphic[2])

    frame += 1

plt.show()