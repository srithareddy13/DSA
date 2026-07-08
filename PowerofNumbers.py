class Solution:
    def reverseexponentiation(self, n):
        MOD = 1000000007

        rev = int(str(n)[::-1])

        ans = 1
        base = n % MOD

        while rev > 0:
            if rev % 2 == 1:
                ans = (ans * base) % MOD
            base = (base * base) % MOD
            rev //= 2

        return ans
