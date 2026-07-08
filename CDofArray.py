class Solution:
    def gcd(self, n, arr):
        def findGCD(a, b):
            while b:
                a, b = b, a % b
            return a

        ans = arr[0]

        for i in range(1, n):
            ans = findGCD(ans, arr[i])

        return ans
