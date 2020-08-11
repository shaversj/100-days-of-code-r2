def valid_solution(board):
    if validate_rows(board) and validate_columns(board) and validate_grids(board):
        return True
    else:
        return False


def validate_rows(board):
    for row in board:
        valid_row_numbers = [num for num in range(1, 10)]
        for num in row:
            if num == 0:
                continue
            if num in valid_row_numbers:
                valid_row_numbers.remove(num)
            else:
                return False

    return True


def validate_columns(board: list):
    for column in range(0, 9):
        valid_column_numbers = [num for num in range(1, 10)]

        for row in range(0, 9):
            num = board[row][column]
            if num == 0:
                continue
            if num in valid_column_numbers:
                valid_column_numbers.remove(num)
            else:
                return False

    return True


def validate_grids(board: list):
    for column in range(0, 9, 3):

        for row in range(0, 9, 3):
            valid_column_numbers = [num for num in range(1, 10)]
            for r in range(row, row + 3):
                for c in range(column, column + 3):
                    num = board[r][c]
                    if num == 0:
                        continue
                    if num in valid_column_numbers:
                        valid_column_numbers.remove(num)
                    else:
                        return False

    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # True

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 0, 3, 4, 8],
                [1, 0, 0, 3, 4, 2, 5, 6, 0],
                [8, 5, 9, 7, 6, 1, 0, 2, 0],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 0, 1, 5, 3, 7, 2, 1, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ])) # False
