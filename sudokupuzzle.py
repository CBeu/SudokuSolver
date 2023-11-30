from sudokusquare import SudokuSquare

class SudokuPuzzle:
    def __init__(self, values=None):
        counter = 0
        validInput = isinstance(values, list) and len(values) == 9 and all(isinstance(sublist, list) and len(sublist) == 9 for sublist in values) and self.isValidPuzzle()
        self.solved = False
        if not validInput:
            self.puzzle = [[SudokuSquare(counter + i + j*9, counter + i + j*9) for i in range(9)] for j in range(9)]
            print("Invalid puzzle input. Puzzle set to default.")
        else:
            self.puzzle = [[SudokuSquare(counter + i + j*9, [item for sublist in values for item in sublist][counter + i + j*9]) for i in range(9)] for j in range(9)]
        self.updated = False

    def __str__(self):
        returnable = ""
        for row in self.puzzle:
            for square in row:
                returnable += str(square) + " "
            returnable += "\n"
        return returnable

    def isValidPuzzle(self):
        #TODO: Implement
        return True
    
    def isSolved(self):
        for row in self.puzzle:
            for square in row:
                if square.value == 0:
                    self.solved = False
                    return False
        self.solved = True
        return True

    def getRow(self, row):
        return self.puzzle[row]

    def getCol(self, col):
        return [row[col] for row in self.puzzle]

    def getBox(self, boxIndex):
        startRowIndex = (boxIndex//3) *3
        startColIndex = (boxIndex%3) * 3
        rows = [self.getRow(i) for i in range(startRowIndex, startRowIndex + 3)]
        box = []
        for row in rows:
            box += row[startColIndex:startColIndex + 3]
        return box

    def updateSquares(self):
        box = 0
        for row in self.puzzle:
            for square in row:
                square.setPossibleValues(self.getRow(square.row), self.getCol(square.column), self.getBox(square.box))
                self.updated = self.updated or square.squareUpdated
                if square.squareUpdated:
                    self.updateSquares()            
        pass

    def updateBox(self):
        self.updatePuzzle(self.getBox)

    def updateRow(self):
        self.updatePuzzle(self.getRow)
        pass

    def updateCol(self):
        self.updatePuzzle(self.getCol)
        pass

    def updatePuzzle(self, func):
        for i in range(9):
            value_counts = {i: 0 for i in range(1, 10)}
            squares = func(i)
            for square in squares:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    value_counts[possibleValue] += 1
            for square in squares:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    if value_counts[possibleValue] == 1 and square.value == 0:
                        square.value = possibleValue
                        square.possibleValues = [possibleValue]
                        square.squareUpdated = True
                        self.updated = True
                        self.updateSquares()
        pass