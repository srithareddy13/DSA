class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        s_count = {}
        g_count = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[s] = s_count.get(s, 0) + 1
                g_count[g] = g_count.get(g, 0) + 1

        cows = 0
        for ch in s_count:
            if ch in g_count:
                cows += min(s_count[ch], g_count[ch])

        return str(bulls) + "A" + str(cows) + "B"
