class Solution:
    def maxSubarraySum(self, arr, k):
        window = sum(arr[:k])
        maximum = window

        for i in range(k, len(arr)):
            window += arr[i]
            window -= arr[i - k]
            maximum = max(maximum, window)

        return maximum
