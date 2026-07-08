class Solution:
    def closestPalindrome(self, num):
        n = int(num)

        if str(n) == str(n)[::-1]:
            return str(n)

        while True:
            n -= 1
            if str(n) == str(n)[::-1]:
                lower = n
                break

        n = int(num)
        while True:
            n += 1
            if str(n) == str(n)[::-1]:
                upper = n
                break

        original = int(num)

        if original - lower <= upper - original:
            return str(lower)
        else:
            return str(upper)
