class SudokuSquare:
    def __init__(self, position, value=None):
        #self.value should be set to 0 if value is None but should be set to value otherwise
        self.value = value if value else 0
        self.possibleValues = [i for i in range(1, 10)]
        self.row = position//9
        self.column = position%9
        self.box = (self.row//3)*3 + self.column//3
        self.updated = False
    
    def __str__(self):
        return str(self.value)
    
    def setPossibleValues(self, row, col, box):
        self.updated = False
        previousPossibleValues = self.possibleValues
        #If self.value is not 0, set possibleValues to self.value and return
        if self.value != 0:
            self.possibleValues = [self.value]
            updated = self.possibleValues != previousPossibleValues
            return
        #get the row the square is in and remove all values in that row from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in row]]
        # get the column the square is in and remove all values in that column from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in col]]
        # get the box the square is in and remove all values in that box from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in box]]
        if len(self.possibleValues) ==1:
            self.value = self.possibleValues[0]

        self.updated = self.possibleValues != previousPossibleValues
        pass

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
        print("Updating squares...")
        box = 0
        for row in self.puzzle:
            for square in row:
                square.setPossibleValues(self.getRow(square.row), self.getCol(square.column), self.getBox(square.box))
                self.updated = self.updated or square.updated
                if square.updated:
                    print("Updated square: ", square.row, square.column, square.possibleValues)
                    self.updateSquares()            
        pass

    def updateBox(self):
        #list all possible values in box (1.....9) use dictionary to keep track of how many times each value appears
        #if a possible value appears only once, set self.value to that value and return
        for box in range(9):
            print("Updating box: ", box)
            value_counts = {i: 0 for i in range(1, 10)}
            box = self.getBox(box)
            for square in box:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    value_counts[possibleValue] += 1
            for square in box:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    if value_counts[possibleValue] == 1:
                        square.value = possibleValue
                        square.possibleValues = [possibleValue]
                        square.updated = True
                        print("Updated square: ", square.row, square.column, square.possibleValues)
                        self.updated = True
                        self.updateSquares()
        pass

    def updateRow(self):
        for row in range(9):
            print("Updating row: ", row)
            value_counts = {i: 0 for i in range(1, 10)}
            row = self.getRow(row)
            for square in row:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    value_counts[possibleValue] += 1
            for square in row:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    if value_counts[possibleValue] == 1:
                        square.value = possibleValue
                        square.possibleValues = [possibleValue]
                        square.updated = True
                        print("Updated square: ", square.row, square.column, square.possibleValues)
                        self.updated = True
                        self.updateSquares()
        pass

    def updateCol(self):
        for col in range(9):
            print("Updating col: ", col)
            value_counts = {i: 0 for i in range(1, 10)}
            col = self.getCol(col)
            for square in col:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    value_counts[possibleValue] += 1
            for square in col:
                if len(square.possibleValues) == 1:
                    continue
                for possibleValue in square.possibleValues:
                    if value_counts[possibleValue] == 1:
                        square.value = possibleValue
                        square.possibleValues = [possibleValue]
                        square.updated = True
                        print("Updated square: ", square.row, square.column, square.possibleValues)
                        self.updated = True
                        self.updateSquares()
        pass


class Solver:
    def __init__(self, inputPuzzle):
        self.puzzle = SudokuPuzzle(inputPuzzle)

    def update(self):
        update_methods = [self.puzzle.updateSquares, self.puzzle.updateBox, self.puzzle.updateRow, self.puzzle.updateCol]
        for method in update_methods:
            method()
            if self.puzzle.isSolved():
                return

    def solve(self):
        loopCount = 0
        while not self.puzzle.isSolved():
            print("Loop: ", loopCount)
            loopCount += 1
            self.update()
            print(self.puzzle)
            if self.puzzle.updated == False and self.puzzle.isSolved() == False:
                print("Puzzle cannot be solved with current algorithm. Please try a different puzzle.")
                break
            self.puzzle.updated = False
            # while True:
            #     proceed = input("Type 'y' to continue: ").lower()
            #     if proceed == 'y':
            #         break
            #     else:
            #         print("Invalid input. Please type 'y' to continue.")
        pass
    

def main():
    rows = []
    easyPuzzleRows = [[3,9,0,8,0,0,0,0,0],
                      [4,1,0,0,0,0,3,7,8],
                      [0,0,0,7,3,2,0,4,0],
                      [7,0,4,0,0,9,0,0,1],
                      [1,0,8,0,4,5,0,2,7],
                      [0,0,5,1,8,0,0,0,3],
                      [0,8,0,0,5,1,0,9,0],
                      [2,0,0,0,0,3,8,0,0],
                      [0,7,1,9,0,0,6,3,0]]
    hardPuzzleRows = [[0,0,0,9,3,4,1,0,5],
                      [3,0,0,0,0,0,0,0,0],
                      [0,4,0,8,0,5,0,9,3],
                      [0,0,0,1,0,0,4,0,0],
                      [0,0,4,0,2,0,8,0,0],
                      [0,0,2,0,4,9,0,0,0],
                      [0,0,6,0,0,0,0,1,0],
                      [0,8,0,7,9,1,0,0,4],
                      [7,0,0,0,0,0,0,0,0]]
    
    choice = input("Enter Type 'y' to enter a row manually or 'n' to use a hard-coded puzzle: ").lower()
    if choice == 'y':
        for i in range(9):
            row = input("Enter row " + str(i) + ": ")
            row = [int(i) for i in row]
            rows.append(row)
    elif choice == 'n':
        choice = input("Enter 'y' to use the easy puzzle or 'n' to use hard: ").lower()
        if choice == 'y':
            rows = easyPuzzleRows
        elif choice == 'n':
            rows = hardPuzzleRows
    else: 
        print("Invalid input. Please type 'y' or 'n'.")
        return

    x = Solver(rows)
    x.solve()

if __name__ == "__main__":
    main()