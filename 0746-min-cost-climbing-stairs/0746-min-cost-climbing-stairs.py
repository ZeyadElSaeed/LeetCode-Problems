class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        plus_one = 0
        plus_two = 0
        
        for i in range( len(cost)-1, -1, -1):
            cur = cost[i] + min(plus_one, plus_two)
            plus_two = plus_one
            plus_one = cur
        
        return min(plus_two, plus_one)
            
        