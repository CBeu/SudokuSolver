from solver import Solver
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
    
    nakedPairRows = [[4,0,0,2,7,0,6,0,0],
                     [7,9,8,1,5,6,2,3,4],
                     [0,2,0,8,4,0,0,0,7],
                     [2,3,7,4,6,8,9,5,1],
                     [8,4,9,5,3,1,7,2,6],
                     [5,6,1,7,9,2,8,4,3],
                     [0,8,2,0,1,5,4,7,9],
                     [0,7,0,0,2,4,3,0,0],
                     [0,0,4,0,8,7,0,0,2]]
    
    choice = input("Enter Type 'y' to enter a row manually or 'n' to use a hard-coded puzzle: ").lower()
    if choice == 'y':
        for i in range(9):
            row = input("Enter row " + str(i) + ": ")
            row = [int(i) for i in row]
            rows.append(row)
    elif choice == 'n':
        choice = input("Enter '1' to use the easy puzzle or '2' to use hard or 3 to use naked pair: ").lower()
        if choice == '1':
            rows = easyPuzzleRows
        elif choice == '2':
            rows = hardPuzzleRows
        elif choice == '3':
            rows = nakedPairRows
    else: 
        print("Invalid input. Please type 'y' or 'n'.")
        return
    print("Input puzzle: ")
    x = Solver(rows)
    print(x.puzzle)
    x.solve()

if __name__ == "__main__":
    main()