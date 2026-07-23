class Solution(object):
    def frequencySort(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return sorted(nums, key=lambda x: (freq[x], -x))
