class Solution(object):
    def findDiagonalOrder(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        ans = []

        for s in range(rows + cols - 1):
            temp = []

            for i in range(rows):
                j = s - i

                if 0 <= j < cols:
                    temp.append(mat[i][j])

            if s % 2 == 0:
                temp.reverse()

            ans.extend(temp)

        return ans
