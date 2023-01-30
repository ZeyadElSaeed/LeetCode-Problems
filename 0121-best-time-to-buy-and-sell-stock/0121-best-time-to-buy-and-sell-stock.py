class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0
        sell_ptr = 1
        profit = 0

        if len(prices) < 2:
            return profit

        while sell_ptr < len(prices):
            profit = max( profit, prices[sell_ptr] - prices[buy_ptr])
            if prices[buy_ptr] > prices[sell_ptr]:
                buy_ptr += 1
                sell_ptr = buy_ptr + 1
            else:
                sell_ptr += 1
        return profit        