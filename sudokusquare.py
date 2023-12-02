class SudokuSquare:
    def __init__(self, position, value=None):
        #self.value should be set to 0 if value is None but should be set to value otherwise
        self.value = value if value else 0
        self.row = position//9
        self.col = position%9
        self.box = (self.row//3)*3 + self.col//3
        self.invalidValues = set()
        self.possibleValues = [i for i in range(1,10)]
    
    def __str__(self):
        return str(self.value)
    
    def addInvalidValue(self, value):
        self.invalidValues.add(value)

    def getPossibleValues(self, puzzle):
        if self.value != 0:
            return self.possibleValues
        self.previousPossibleValues = self.possibleValues
        possibleColValues = [value for value in range(1,10) if value not in [square.value for square in puzzle.getRow(self.row)]]
        possibleRowValues = [value for value in range(1,10) if value not in [square.value for square in puzzle.getCol(self.col)]]
        possibleBoxValues = [value for value in range(1,10) if value not in [square.value for square in puzzle.getBox(self.box)]]
        self.possibleValues = list(set(possibleColValues).intersection(possibleRowValues, possibleBoxValues) - self.invalidValues)
        if len(self.possibleValues) == 1:
            self.value = self.possibleValues[0]
        return self.possibleValues