class Solution(object):
    def minWindow(self, s, t):
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        left = 0
        count = 0
        best = ""

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] <= need[ch]:
                count += 1

            while count == len(t):
                if best == "" or right - left + 1 < len(best):
                    best = s[left:right + 1]

                old = s[left]
                window[old] -= 1

                if old in need and window[old] < need[old]:
                    count -= 1

                left += 1

        return best
