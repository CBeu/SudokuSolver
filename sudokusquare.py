class SudokuSquare:
    def __init__(self, position, value=None):
        #self.value should be set to 0 if value is None but should be set to value otherwise
        self.value = value if value else 0
        self.possibleValues = [i for i in range(1, 10)]
        self.row = position//9
        self.column = position%9
        self.box = (self.row//3)*3 + self.column//3
        self.squareUpdated = False
    
    def __str__(self):
        return str(self.value)
    

    #this is going to always overwite possibleValues with a new list of possible values, write another method to update possibleValues
    def setPossibleValues(self, row, col, box):
        self.squareUpdated = False
        previousPossibleValues = self.possibleValues
        #If self.value is not 0, set possibleValues to self.value and return
        if self.value != 0:
            self.possibleValues = [self.value]
            self.squareUpdated = self.possibleValues != previousPossibleValues
            return
        #get the row the square is in and remove all values in that row from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in row]]
        # get the column the square is in and remove all values in that column from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in col]]
        # get the box the square is in and remove all values in that box from possibleValues
        self.possibleValues = [value for value in self.possibleValues if value not in [square.value for square in box]]
        if len(self.possibleValues) > len(previousPossibleValues):
            print("uhoh")
        if len(self.possibleValues) ==1:
            self.value = self.possibleValues[0]

        self.squareUpdated = self.possibleValues != previousPossibleValues
        pass