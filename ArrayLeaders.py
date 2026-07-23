class Solution:
    def leaders(self, arr):
        ans = []
        maxi = arr[-1]
        ans.append(maxi)

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= maxi:
                maxi = arr[i]
                ans.append(arr[i])

        return ans[::-1]
