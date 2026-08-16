class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        minimum = len(nums) + 1

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minimum = min(minimum, right - left + 1)
                total -= nums[left]
                left += 1

        if minimum == len(nums) + 1:
            return 0

        return minimum
