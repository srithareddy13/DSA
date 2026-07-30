from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            cur = q.popleft()

            if isValid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue
                nxt = cur[:i] + cur[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res
