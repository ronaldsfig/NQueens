import random


class Chessboard:
    def __init__(self, size):
        self.size = size
        self.board = [None] + [0] * size

    def generateFirstPositions(self):
        for i in range(1, len(self.board)):
            self.board[i] = i

    def swapPositions(self, x, y):
        if x < 1 or x > self.size or y < 1 or y > self.size:
            print("Índice inválido.")
            return

        self.board[x], self.board[y] = self.board[y], self.board[x]

    def displayChessboard(self):
        for i in range(1, self.size + 1):
            row = ""
            for j in range(1, self.size + 1):
                if self.board[j] == i:
                    row += " O "
                else:
                    row += " - "
            print(row)

    def fitness(self):
        for i in range(1, self.size):
            right_diagonal_a = self.board[i]-i
            left_diagonal_a = self.board[i]+i

            for j in range(1, self.size):
                if i != j:
                    right_diagonal_b = self.board[j]-j
                    left_diagonal_b = self.board[j]+j

                    if (right_diagonal_a == right_diagonal_b) or (left_diagonal_a == left_diagonal_b):
                        return True

        # depois ver a questao das diagonais extremas

        return False

    def randomPositions(self):
        x = random.randint(1, self.size)
        y = random.randint(1, self.size)
        return x, y

    def disturbance(self):
        # Método para introduzir uma perturbação no tabuleiro.
        # Isso pode envolver trocar aleatoriamente duas posições.
        pass

    def cooling(self, temperature):
        # Método para reduzir a temperatura do algoritmo de recozimento simulado.
        # Você precisa implementar a lógica para reduzir a temperatura.
        pass

    def simulatedAnnealing(self, temperature):
        # Método principal para executar o algoritmo de recozimento simulado.
        # Você precisa implementar a lógica para realizar o recozimento simulado.
        pass
