class Solution:
    def powerSet(self, s):
        ans = []

        def solve(index, curr):
            if index == len(s):
                ans.append(curr)
                return

            # Include current character
            solve(index + 1, curr + s[index])

            # Exclude current character
            solve(index + 1, curr)

        solve(0, "")
        ans.sort()
        return ans
