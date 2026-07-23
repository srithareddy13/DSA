class Solution:
    def winner(self, arr):
        votes = {}

        for name in arr:
            votes[name] = votes.get(name, 0) + 1

        max_votes = max(votes.values())
        winner = min(name for name, count in votes.items() if count == max_votes)

        return [winner, max_votes]
