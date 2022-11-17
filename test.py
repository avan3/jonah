import random, copy, time

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides 

    def roll(self):
        self.value = random.randint(1, self.sides)

class Board:
    def __init__(self, numSides = 6, numDice = 5):
        board = []
        for _ in range(numDice):
            board.append(Dice(numSides))
        self.board = board
        self.numDice = numDice 
        self.maxScore = numDice * numSides

    def shuffle(self):
        for dice in self.board:
            dice.roll()

class Rules:
    def removeAllValuesFromBoard(self, board, value = 3):
        board = [v for v in board if v != value]
        return 0

    def countLowestDice(self, board):
        lowest = min(board, key=lambda dice: dice.value)
        board.remove(lowest)
        return lowest.value

class Game:
    def __init__(self, board, rules, iterations):
        self.board = board 
        self.rules = rules 
        self.scores = [0] * (self.board.maxScore + 1)
        self.iterations = iterations

    def play(self):
        for i in range(self.iterations + 1):
            board = copy.deepcopy(self.board)
            score = 0
            while len(board.board) > 0:
                board.shuffle()
                score += self.rules.removeAllValuesFromBoard(board.board, 3)
                score += self.rules.countLowestDice(board.board)
            self.scores[score] += 1

    def printScore(self):
        print(f"Number of simulations was {self.iterations} using {self.board.numDice} dice.")

        start = time.time()
        for i in range(self.board.maxScore + 1):
            print(f"Total {i} occurs {round(self.scores[i]/self.iterations, 2)} occurred {self.scores[i]} times.")
        end = time.time()
        timeElapsed = end - start

        print(f"Total simulation took {round(timeElapsed, 1)} seconds.")

def main():
    board = Board(6, 2)
    rules = Rules()
    game = Game(board, rules, 100)

    game.play()
    game.printScore()

main()
