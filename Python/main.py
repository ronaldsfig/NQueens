from chessboard import Chessboard
import time

size = 64
runs = 10
average = 0

for i in range(1, runs + 1):
    chessboard = Chessboard(size)

    start = time.time()
    chessboard.simulatedAnnealing(4000)
    end = time.time() - start
    print("Runtime ", i, " in second:", end)

    average += end

average /= runs
print("Avarage: ", average)
