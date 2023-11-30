class SudokuSquare:
    def __init__(self, position, value=None):
        #self.value should be set to 0 if value is None but should be set to value otherwise
        self.value = value if value else 0
        self.possibleValues = [i for i in range(1, 10)]
        self.row = position//9
        self.column = position%9
        self.box = (self.row//3)*3 + self.column//3
    
    def __str__(self):
        return str(self.value)
    
    def setPossibleValues(self):
        # Your code here
        '''
        1. If self.value is not 0, set possibleValues to self.value and return
        2. If self.value is 0, set possibleValues to [1, 2, 3, 4, 5, 6, 7, 8, 9]
            a. get the row the square is in and remove all values in that row from possibleValues
            b. get the column the square is in and remove all values in that column from possibleValues
            c. get the box the square is in and remove all values in that box from possibleValues
        '''
        pass

class SudokuPuzzle:
    def __init__(self):
        counter = 0
        self.puzzle = [[SudokuSquare(counter + i + j*9, counter + i + j*9) for i in range(9)] for j in range(9)]

    def isValidPuzzle(self):
        # Your code here
        pass

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


class Solver:
    def __init__(self):
        self.puzzle = SudokuPuzzle()

    
    def solve(self):
        # Your code here
        pass
    

def main():
    # Your code here
    x = SudokuPuzzle()
    y = x.getBox(8)
    for box in y:
        print(box, box.row, box.column, box.box)

if __name__ == "__main__":
    main()



'''Notes:
1. Solver class should accept a sudoku puzzle as an input
    a. The puzzle should be a 2D array of integers
    b. The puzzle should be a 9x9 grid
    c. The puzzle should be a valid sudoku puzzle
2. Solver class should have a solve method that returns a solved sudoku puzzle
'''
