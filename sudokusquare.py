class SudokuSquare:
    def __init__(self, position, value=None):
        #self.value should be set to 0 if value is None but should be set to value otherwise
        self.value = value if value else 0
        self.row = position//9
        self.col = position%9
        self.box = (self.row//3)*3 + self.col//3
        self.possibleValues = []
    
    def __str__(self) -> str:
        return str(self.value)

    def getPossibleValues(self, puzzle) ->list[int]:
        if self.value != 0:
            return list(self.value)
        allValues = set(range(1,10))
        possibleColValues = set(square.value for square in puzzle.getRow(self.row))
        possibleRowValues = set(square.value for square in puzzle.getCol(self.col))
        possibleBoxValues = set(square.value for square in puzzle.getBox(self.box))
        #Return a list of possible values that are in all three lists
        self.possibleValues = list(allValues-possibleColValues-possibleRowValues-possibleBoxValues)
        return self.possibleValues
