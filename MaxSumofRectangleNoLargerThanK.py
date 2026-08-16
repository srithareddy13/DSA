class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        rows = len(matrix)
        cols = len(matrix[0])
        ans = float('-inf')

        for left in range(cols):
            row_sum = [0] * rows

            for right in range(left, cols):
                for i in range(rows):
                    row_sum[i] += matrix[i][right]

                for i in range(rows):
                    total = 0

                    for j in range(i, rows):
                        total += row_sum[j]

                        if total <= k:
                            ans = max(ans, total)

        return ans
