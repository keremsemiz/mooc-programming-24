# Write your solution here
def transpose(matrix: list):
    for row in range(len(matrix)):
        for column in range(row, len(matrix)):
            num = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = num


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
