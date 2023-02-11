class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = 0
        for account in accounts:
            maximum_wealth = max( maximum_wealth, sum(account))
        return maximum_wealth

    
    
        