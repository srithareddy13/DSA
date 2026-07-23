class Solution:
    def firstRepChar(self, s):
        seen = set()

        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)

        return "-1"
