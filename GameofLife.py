class Solution(object):
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        new_board = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                live = 0

                # Check 8 neighbours
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:

                        if di == 0 and dj == 0:
                            continue

                        ni = i + di
                        nj = j + dj

                        if 0 <= ni < rows and 0 <= nj < cols:
                            live += board[ni][nj]

                # Game of Life rules
                if board[i][j] == 1:
                    if live == 2 or live == 3:
                        new_board[i][j] = 1
                else:
                    if live == 3:
                        new_board[i][j] = 1

        # Copy new board back
        for i in range(rows):
            for j in range(cols):
                board[i][j] = new_board[i][j]
