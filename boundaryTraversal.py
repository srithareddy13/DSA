class Solution:
    def boundaryTraversal(self, mat):
        n = len(mat)
        m = len(mat[0])
        ans = []

        # Only one row
        if n == 1:
            return mat[0]

        # Only one column
        if m == 1:
            for i in range(n):
                ans.append(mat[i][0])
            return ans

        # Top row
        for j in range(m):
            ans.append(mat[0][j])

        # Right column
        for i in range(1, n):
            ans.append(mat[i][m - 1])

        # Bottom row (right to left)
        for j in range(m - 2, -1, -1):
            ans.append(mat[n - 1][j])

        # Left column (bottom to top)
        for i in range(n - 2, 0, -1):
            ans.append(mat[i][0])

        return ans
