class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        buy, sell = 0, 1
        max_profit = 0

        while sell < n:
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            else:
                max_profit = max(max_profit, profit)
            sell += 1
            print(f"{profit}, {max_profit}")
        
        return max_profit