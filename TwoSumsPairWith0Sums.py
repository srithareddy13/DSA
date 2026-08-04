class Solution:
    def getPairs(self, arr):
        s = set(arr)
        ans = []

        for x in s:
            if x < 0 and -x in s:
                ans.append([x, -x])

        # Handle the pair (0, 0)
        if arr.count(0) >= 2:
            ans.append([0, 0])

        ans.sort()
        return ans
