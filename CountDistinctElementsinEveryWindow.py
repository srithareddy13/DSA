class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        ans = []

        # First window
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1

        ans.append(len(freq))

        # Slide the window
        for i in range(k, len(arr)):
            # Add new element
            freq[arr[i]] = freq.get(arr[i], 0) + 1

            # Remove old element
            old = arr[i - k]
            freq[old] -= 1

            if freq[old] == 0:
                del freq[old]

            ans.append(len(freq))

        return ans
