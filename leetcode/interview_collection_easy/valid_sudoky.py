'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
'''
import itertools
from typing import List

'''
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                # square = list(itertools.chain(row[j:j + 3] for row in grid[i:i + 3]))

                # https://www.youtube.com/watch?v=TjFXEUCMqI8
                idx = (r // 3) * 3 + c // 3  # 0, 1, 2,3,4,5,6,7 squares
                # 1 //
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

print(Solution().isValidSudoku(board=board))


def sudoku_ok(line):
    return (len(line) == 9 and sum(line) == sum(set(line)))


def check_sudoku(grid):
    bad_rows = [row for row in grid if not sudoku_ok(row)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_ok(col)]
    squares = []
    for i in range(9, step=3):
        for j in range(9, step=3):
          square = list(itertools.chain(row[j:j + 3] for row in grid[i:i + 3]))
          squares.append(square)
    bad_squares = [square for square in squares if not sudoku_ok(square)]
    return not (bad_rows or bad_cols or bad_squares)


# where the squares are numbered as follows:
# 0 1 2
# 3 4 5
# 6 7 8

s = 3 # second row, first column
r = int(s/3) # r = 1
c =  s%3  # c = 0

my_list = [element for row in board[r*3:r*3+3]
           for element in row[c*3:c*3+3]]


# Python3 program to check whether
# given sudoku board is valid or not

# Checks whether there is any
# duplicate in current row or not
def notInRow(arr, row):
    # Set to store characters seen so far.
    st = set()

    for i in range(0, 9):

        # If already encountered before,
        # return false
        if arr[row][i] in st:
            return False

        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            st.add(arr[row][i])

    return True


# Checks whether there is any
# duplicate in current column or not.
def notInCol(arr, col):
    st = set()

    for i in range(0, 9):

        # If already encountered before,
        # return false
        if arr[i][col] in st:
            return False

        # If it is not an empty cell, insert
        # value at the current cell in the set
        if arr[i][col] != '.':
            st.add(arr[i][col])

    return True


# Checks whether there is any duplicate
# in current 3x3 box or not.
def notInBox(arr, startRow, startCol):
    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]

            # If already encountered before,
            # return false
            if curr in st:
                return False

            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != '.':
                st.add(curr)

    return True


# Checks whether current row and current
# column and current 3x3 box is valid or not
def isValid(arr, row, col):
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))


def isValidConfig(arr, n):
    for i in range(0, n):
        for j in range(0, n):

            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not isValid(arr, i, j):
                return False

    return True


# Drivers code
if __name__ == "__main__":

    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    if isValidConfig(board, 9):
        print("YES")
    else:
        print("NO")