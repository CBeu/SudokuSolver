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
        print("Backtracking...")
        if self.backTrack(squares):
            print("Result: ")
            print(self.puzzle)
            print("Rounds: " + str(self.rounds))
        else:
            print("No solution found.")
    
    def initialize(self, squares:[SudokuSquare]):
        self.incrementRounds()
        for square in squares:
            if square.value == 0:
                if len(square.getPossibleValues(self.puzzle)) == 1:
                    square.value = square.getPossibleValues(self.puzzle)[0]
                    self.initialize(squares)
        pass

    def backTrack(self, squares:[SudokuSquare]):
        self.incrementRounds()
        #Check to see if the puzzle is solved
        if self.puzzle.isSolved():
            print("Solved with backtracking.")
            return True
        #Go through each square and try each possible value
        for square in squares:
            #Check to see if the square already has a value
            if square.value == 0:
                possibleValues = square.getPossibleValues(self.puzzle)
                for value in possibleValues:
                    #Try to solve the puzzle with the value from possible values
                    square.value = value
                    #Check to see if the puzzle is solved after trying the value
                    if self.backTrack(squares):
                        return True
                    #If the puzzle is not solved, backtrack
                    square.value = 0
                #If no possible values work, return False
                return False
        print("Backtrack failed.")
        return False

    