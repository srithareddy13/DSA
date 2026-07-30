class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        if n == 0:
            return 0
        return (2 ** n) - 1
