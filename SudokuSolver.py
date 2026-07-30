class Solution(object):
    def solveSudoku(self, board):
        def is_valid(row, col, ch):
            # Check row
            for j in range(9):
                if board[row][j] == ch:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == ch:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == ch:
                        return False

            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for ch in "123456789":
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        solve()
