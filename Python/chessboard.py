import random
import math
import copy

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
        numbers = list(range(1, self.size + 1))
        random.shuffle(numbers)
        row = 1

        while len(numbers) > 0:
            column = numbers.pop()
            self.board[row] = column
            row += 1


    def threatCalculate(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        return (n - 1) * n / 2


    def fitness(self):
        fit = 0
        right_diagonals = {}
        left_diagonals = {}

        for i in range(1, self.size+1):
            right_diagonal = self.board[i]-i
            left_diagonal = self.board[i]+i

            if right_diagonal not in right_diagonals:
                right_diagonals[right_diagonal] = 1
            else:
                right_diagonals[right_diagonal] += 1

            if left_diagonal not in left_diagonals:
                left_diagonals[left_diagonal] = 1
            else:
                left_diagonals[left_diagonal] += 1

        for i in right_diagonals:
            fit += self.threatCalculate(right_diagonals[i])
        
        for i in left_diagonals:
            fit += self.threatCalculate(left_diagonals[i])

        return fit
    

    def simulatedAnnealing(self, temperature):
        self.generateFirstPositions()
        solution = [copy.deepcopy(self.board), self.fitness()]

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
            else:
                probability = random.uniform(0, 1) < math.exp(-delta / temperature)
                
                if probability:
                    solution = new_solution
                else:
                    self.board = copy.deepcopy(solution[0])

            iteration += 1