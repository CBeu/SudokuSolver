from sudokupuzzle import SudokuPuzzle
from sudokusquare import SudokuSquare

class Solver:
    def __init__(self, inputPuzzle):
        self.puzzle = SudokuPuzzle(inputPuzzle)
        self.rounds = 0

    def incrementRounds(self):
        self.rounds += 1
        
    def solve(self):
        squares = [square for row in self.puzzle.puzzle for square in row]
        print("Initializing...")
        self.initialize(squares)
        if self.puzzle.isSolved():
            print("Solved without backtracking.")
            return
        print("Initialized.")
        self.backTrack(squares)
        print("Result: ")
        print(self.puzzle)
        print("Rounds: " + str(self.rounds))
    
    def initialize(self, squares:[SudokuSquare]):
        for square in squares:
            if square.value == 0:
                if len(square.getPossibleValues(self.puzzle)) == 1:
                    square.value = square.getPossibleValues(self.puzzle)[0]
                    self.initialize(squares)
        pass

    def backTrack(self, squares:[SudokuSquare]):
        self.incrementRounds()
        if self.puzzle.isSolved():
            print("Solved with backtracking.")
            return True
        for square in squares:
            if square.value == 0:
                possibleValues = square.getPossibleValues(self.puzzle)
                for value in possibleValues:
                    square.value = value
                
                    if self.backTrack(squares):
                        return True
                    square.value = 0
                return False
        print("Backtrack failed.")
        return False

    