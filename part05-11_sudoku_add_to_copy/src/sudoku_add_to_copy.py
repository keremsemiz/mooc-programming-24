# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = "_"


    for newRow in range(9):
        if newRow > 0 and newRow % 3 == 0:
            print()
        
        for newCol in range(9):
            print(sudoku[newRow][newCol], end=" ")
            if (newCol + 1) % 3 == 0:
                print(end=" ")
        print()



def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
        newsudoku = [row[:] for row in sudoku]
        newsudoku[row_no][column_no] = number

        return newsudoku


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)