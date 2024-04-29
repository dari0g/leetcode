class Solution:
    def maxProfit(prices) -> int:
            buying_price = prices[0]
            max_profit = 0
            current_profit = 0
            for i in range(1, len(prices)):
                if prices[i] > buying_price:
                    current_profit = prices[i] - buying_price
                    if current_profit > max_profit:
                        max_profit = current_profit
                elif prices[i] < buying_price:
                    buying_price = prices[i]
                
            return max_profit