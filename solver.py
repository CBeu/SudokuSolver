from sudokupuzzle import SudokuPuzzle

class Solver:
    def __init__(self, inputPuzzle):
        self.puzzle = SudokuPuzzle(inputPuzzle)

    def update(self):
        update_methods = [self.puzzle.updateSquares, self.puzzle.updateBox, self.puzzle.updateRow, self.puzzle.updateCol]
        solveStrategies = [self.nakedPair]
        for method in update_methods:
            method()
            if self.puzzle.isSolved():
                return
        for strategy in solveStrategies:
            strategy()
            if self.puzzle.isSolved():
                return

    def removeNakedPairs(self, nakedPairs, square):
        for pair in nakedPairs:
            if square.possibleValues == [pair[0],pair[1]]:
                print("Skipping square: ", square.row, square.column, square.possibleValues, " because it is a naked pair")
                return
            for i in range(2):
                if pair[i] in square.possibleValues:
                    print("removed ", pair[i], "from square: ", square.row, square.column, square.possibleValues)
                    square.possibleValues.remove(pair[i])
                    square.squareUpdated = True
            if len(square.possibleValues) == 1 and square.value == 0:
                square.value = square.possibleValues[0]
                square.possibleValues = [square.value]
                square.squareUpdated = True
                print("Updated square values: ", square.row, square.column, square.possibleValues)
        pass
    def nakedPair(self):
        dataSelectors = [self.puzzle.getBox, self.puzzle.getRow, self.puzzle.getCol]
        for selector in dataSelectors:
            for i in range(9):
                nakedPairs = set([])
                data = selector(i)
                for square in data:
                    if len(square.possibleValues) == 2:
                        for otherSquare in data:
                            if square != otherSquare and square.possibleValues == otherSquare.possibleValues:
                                nakedPairs.add((square.possibleValues[0], square.possibleValues[1]))
                for square in data:
                    self.removeNakedPairs(nakedPairs, square)
        pass

    def solve(self):
        loopCount = 0
        while not self.puzzle.isSolved():
            print("Loop: ", loopCount)
            if loopCount > 0 and self.puzzle.updated == False and self.puzzle.isSolved() == False:
                print("Puzzle cannot be solved with current algorithm. Please try a different puzzle.")
                break
            loopCount += 1
            self.update()
            print(self.puzzle)
            self.puzzle.updated = False
            for squares in self.puzzle.puzzle:
                for square in squares:
                    square.squareUpdated = False
        pass