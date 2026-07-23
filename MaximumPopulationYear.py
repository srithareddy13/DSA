class Solution(object):
    def maximumPopulation(self, logs):
        years = [0] * 101  # 1950 to 2050

        for birth, death in logs:
            years[birth - 1950] += 1
            years[death - 1950] -= 1

        max_pop = 0
        curr = 0
        ans = 1950

        for i in range(101):
            curr += years[i]
            if curr > max_pop:
                max_pop = curr
                ans = 1950 + i

        return ans
