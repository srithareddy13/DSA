class Solution:
	def getCount(self, n):
		moves={
		    0:[0,8],
		    1:[1,2,4],
		    2:[2,1,3,5],
		    3:[3,2,6],
		    4:[4,1,5,7],
		    5:[5,2,4,6,8],
		    6:[6,3,5,7],
		    7:[7,4,8],
		    8:[8,5,7,9,0],
		    9:[9,6,8]
		}
		dp=[1]*10
		for _ i range (n-1):
		    ne=[0]*10
		    for d in range (10):
		        for t in moves[d]:
		            ne[d]+=dp[t]
		    dp=ne
		 return sum(dp)
