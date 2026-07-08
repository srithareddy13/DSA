class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 1000000007

        even = (n + 1) // 2
        odd = n // 2

        return (pow(5, even, MOD) * pow(4, odd, MOD)) % MOD
