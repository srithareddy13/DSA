class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0

        # Find candidate
        for num in arr:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Verify candidate
        count = 0
        for num in arr:
            if num == candidate:
                count += 1

        if count > len(arr) // 2:
            return candidate
        return -1
