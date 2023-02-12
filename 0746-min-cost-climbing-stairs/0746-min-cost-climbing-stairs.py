class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp_cost = [0] * (n+2)
        
        for i in range(n-1, -1, -1):
            dp_cost[i] = cost[i] + min(dp_cost[i+1], dp_cost[i+2])
        
        return min(dp_cost[0], dp_cost[1])
            
        