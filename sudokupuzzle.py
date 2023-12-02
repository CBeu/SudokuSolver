from sudokusquare import SudokuSquare

class SudokuPuzzle:
    def __init__(self, values=None):
        counter = 0
        validInput = isinstance(values, list) and len(values) == 9 and all(isinstance(sublist, list) and len(sublist) == 9 for sublist in values)
        self.puzzle = [[]]
        if not validInput:
            raise ValueError("Invalid puzzle input dimensions. Puzzle set to default.")
        else:
            self.puzzle = [[SudokuSquare(counter + i + j*9, [item for sublist in values for item in sublist][counter + i + j*9]) for i in range(9)] for j in range(9)]
            if self.isValidPuzzle():
                pass
            else:
                raise ValueError("Invalid puzzle input values. Puzzle set to default.")

    def __str__(self):
        returnable = ""
        for row in self.puzzle:
            for square in row:
                returnable += str(square) + " "
            returnable += "\n"
        return returnable
    
    def isValidPuzzle(self):
        for i in range(9):
            row = [square.value for square in self.getRow(i) if square.value != 0]
            col = [square.value for square in self.getCol(i) if square.value != 0]
            box = [square.value for square in self.getBox(i) if square.value != 0]
            if not len(row) == len(set(row)) or not len(col) == len(set(col)) or not len(box) == len(set(box)):
                return False
        return True

    def isSolved(self):
        for row in self.puzzle:
            for square in row:
                if square.value == 0:
                    return False
        return True and self.isValidPuzzle()

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