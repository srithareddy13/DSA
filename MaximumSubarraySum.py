class Solution:
    def maxSubarraySum(self, arr):
        current = arr[0]
        maximum = arr[0]

        for i in range(1, len(arr)):
            current = max(arr[i], current + arr[i])
            maximum = max(maximum, current)

        return maximum
