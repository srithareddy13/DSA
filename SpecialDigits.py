class Solution:
    def bestNumbers(self, n, a, b, c, d):
        MOD = 1000000007

        # Special case: if both digits are same
        if a == b:
            s = n * a
            if s == 0:
                return 1 if (c == 0 or d == 0) else 0
            while s:
                digit = s % 10
                if digit == c or digit == d:
                    return 1
                s //= 10
            return 0

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            invfact[i - 1] = (invfact[i] * i) % MOD

        ans = 0

        for i in range(n + 1):
            s = i * a + (n - i) * b

            ok = False
            if s == 0:
                ok = (c == 0 or d == 0)
            else:
                t = s
                while t:
                    digit = t % 10
                    if digit != c and digit != d:
                        ok = False
                        break
                    ok = True
                    t //= 10

            if ok:
                ways = fact[n]
                ways = (ways * invfact[i]) % MOD
                ways = (ways * invfact[n - i]) % MOD
                ans = (ans + ways) % MOD

        return ans
