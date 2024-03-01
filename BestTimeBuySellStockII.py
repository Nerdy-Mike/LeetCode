class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0 
        max_profit = 0 
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price 
                total_profit += max_profit
                min_price = price
                max_profit = 0

        return total_profit
