class Solution:
    def snakePattern(self, matrix):
        ans = []

        for i in range(len(matrix)):
            if i % 2 == 0:
                for j in range(len(matrix[i])):
                    ans.append(matrix[i][j])
            else:
                for j in range(len(matrix[i]) - 1, -1, -1):
                    ans.append(matrix[i][j])

        return ans
