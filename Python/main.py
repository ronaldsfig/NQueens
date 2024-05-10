import time
import random


class Board(object):
    """An N-queens solution attempt."""

    def __init__(self, queens):
        """Instances differ by their queen placements."""
        self.queens = queens.copy()  # No aliasing!

    def display(self):
        """Print the board."""
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print 'Q',
                else:
                    print '-',
            print
        print

    def moves(self):
        """Return a list of possible moves given the current placements."""
        # YOU FILL THIS IN

    def neighbor(self, move):
        """Return a Board instance like this one but with one move made."""
        # YOU FILL THIS IN

    def cost(self):
        """Compute the cost of this solution."""
        # YOU FILL THIS IN


class Agent(object):
    """Knows how to solve an n-queens problem with simulated annealing."""

    def anneal(self, board):
        """Return a list of moves to adjust queen placements."""
        # YOU FILL THIS IN


def main():
    """Create a problem, solve it with simulated anealing, and console-animate."""

    queens = dict()
    for col in range(8):
        row = random.choice(range(8))
        queens[col] = row

    board = Board(queens)
    board.display()

    agent = Agent()
    path = agent.anneal(board)

    while path:
        move = path.pop(0)
        board = board.neighbor(move)
        time.sleep(0.1)
        board.display()


if __name__ == '__main__':
    main()
