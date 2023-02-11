class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = []
        # first 3 numbers are fixed 
        dp.append(0)
        dp.append(1)
        dp.append(2)
        
        for i in range( 3, n+1 ):
            val = dp[i-1] + dp[i-2]
            dp.append(val)
        
        return dp[n]
        
        