class Solution(object):
    def spiralOrder(self, matrix):
        ans = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Top row → left to right
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            # Right column → top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Bottom row → right to left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            # Left column → bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
