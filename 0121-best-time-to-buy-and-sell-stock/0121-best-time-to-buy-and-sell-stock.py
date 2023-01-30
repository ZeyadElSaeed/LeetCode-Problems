class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit = 0

        if len(prices) < 2:
            return profit

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            profit = max( profit, price - lowest_price)
        return profit        