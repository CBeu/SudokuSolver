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
    
    def setPossibleValues(self, row, col, box):
        # Your code here
        #1. If self.value is not 0, set possibleValues to self.value and return
        if self.value != 0:
            self.possibleValues = [self.value]
            return
        #    a. get the row the square is in and remove all values in that row from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in row]]
        #    b. get the column the square is in and remove all values in that column from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in col]]
        #    c. get the box the square is in and remove all values in that box from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in box]]
        if len(self.possibleValues) ==1:
            self.value = self.possibleValues[0]
        pass

class SudokuPuzzle:
    def __init__(self, values=None):
        counter = 0
        validInput = isinstance(values, list) and len(values) == 9 and all(isinstance(sublist, list) and len(sublist) == 9 for sublist in values)
        print("validInput", validInput)
        if not validInput:
            self.puzzle = [[SudokuSquare(counter + i + j*9, counter + i + j*9) for i in range(9)] for j in range(9)]
            print("Invalid puzzle input. Puzzle set to default.")
        else:
            self.puzzle = [[SudokuSquare(counter + i + j*9, [item for sublist in values for item in sublist][counter + i + j*9]) for i in range(9)] for j in range(9)]


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

    def updateSquares(self):
        for row in self.puzzle:
            for square in row:
                square.setPossibleValues(self.getRow(square.row), self.getCol(square.column), self.getBox(square.box))
                print(square, square.possibleValues)
        pass


class Solver:
    def __init__(self):
        self.puzzle = SudokuPuzzle()

    
    def solve(self):
        # Your code here
        pass
    

def main():
    # Your code here
    x = SudokuPuzzle([[3,9,0,8,0,0,0,0,0],
                      [4,1,0,0,0,0,3,7,8],
                      [0,0,0,7,3,2,0,4,0],
                      [7,0,4,0,0,9,0,0,1],
                      [1,0,8,0,4,5,0,2,7],
                      [0,0,5,1,8,0,0,0,3],
                      [0,8,0,0,5,1,0,9,0],
                      [2,0,0,0,0,3,8,0,0],
                      [0,7,1,9,0,0,6,3,0]])
    flag = True
    while flag:
        x.updateSquares()
        print("--------------------")
        while True:
            proceed = input("Type 'y' to continue: ")
            if proceed.lower() == 'y':
                break
            elif proceed.lower() == 'n':
                flag = False
                break
    # y = x.getBox(8)
    # for box in y:
    #     print(box, box.row, box.column, box.box)
    #     pass

if __name__ == "__main__":
    main()