class Solution:
    def fib(self, n: int) -> int:
        
        # using Recursion
        def recursion(n):
            if n == 0 or n == 1:
                return n
            return recursion(n-1) + recursion(n-2)
        
        # using dynamic programming
        def dynamic(n):
            if n == 0 or n == 1:
                return n
            dp = [0]*(n+1)
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]
        
        return dynamic(n)
        