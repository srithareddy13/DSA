class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []

        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(matrix[i][j])
            ans.append(row)

        return ans
