class Solution(object):
    def myPow(self, x, n):
        if n<0:
            x=1/x
            n=-n
        ans=x
        res=1
        while n!=0:
            if n&1==1:
                res=res*ans
            ans=ans*ans
            n=n>>1
