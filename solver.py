from sudokupuzzle import SudokuPuzzle
from sudokusquare import SudokuSquare

class Solver:
    def __init__(self, inputPuzzle):
        self.puzzle = SudokuPuzzle(inputPuzzle)
        self.rounds = 0

    def incrementRounds(self):
        self.rounds += 1
    '''
    while not puzzle.isSolved():
    
    '''
    def solve(self):
        squares = [square for row in self.puzzle.puzzle for square in row]
        print("Initializing...")
        self.initialize(squares)
        if self.puzzle.isSolved():
            print("Solved without backtracking.")
            return
        print("Initialized.")
        self.backTrack(squares)
    
    def initialize(self, squares:[SudokuSquare]):
        self.incrementRounds()
        for square in squares:
            if square.value == 0:
                if len(square.getPossibleValues(self.puzzle)) == 1:
                    self.initialize(squares)
        pass

    def backTrack(self, squares:[SudokuSquare]):
        print("Backtracking...")
        self.incrementRounds()
        if self.puzzle.isSolved():
            return
        for square in squares:
            if square.value != 0:
                
                pass
            pass
        pass

    def makeGuess(self, square: SudokuSquare):
        print("Guessing...")
        guess = square.getPossibleValues(self.puzzle)[0]
        pass