class Solution:
    def missingNumber(self, arr):
        s = set(arr)
        ans = 1

        while ans in s:
            ans += 1

        return ans
