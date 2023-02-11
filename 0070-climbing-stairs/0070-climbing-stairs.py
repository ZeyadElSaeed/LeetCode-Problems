class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        
        prev_prev = 0
        prev = 1
        
        for i in range( n ):
            temp_val = prev
            prev = prev_prev + prev
            prev_prev = temp_val 
        
        return prev
        
        