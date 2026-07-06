class Solution:
    def isPrime(self, n):
        # code here
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    return False
            return True
        else:
            return False
