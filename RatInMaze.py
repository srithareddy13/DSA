class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        ans = []

        if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return ans

        visited = [[False] * n for _ in range(n)]

        def solve(x, y, path):
            if x == n - 1 and y == n - 1:
                ans.append(path)
                return

            visited[x][y] = True

            # Down
            if x + 1 < n and maze[x + 1][y] == 1 and not visited[x + 1][y]:
                solve(x + 1, y, path + "D")

            # Left
            if y - 1 >= 0 and maze[x][y - 1] == 1 and not visited[x][y - 1]:
                solve(x, y - 1, path + "L")

            # Right
            if y + 1 < n and maze[x][y + 1] == 1 and not visited[x][y + 1]:
                solve(x, y + 1, path + "R")

            # Up
            if x - 1 >= 0 and maze[x - 1][y] == 1 and not visited[x - 1][y]:
                solve(x - 1, y, path + "U")

            visited[x][y] = False

        solve(0, 0, "")
        return ans
