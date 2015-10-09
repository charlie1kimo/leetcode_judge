"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if prices == None or len(prices) < 2:
            return 0

        max_profit = 0
        min_price = prices[0]
        for index in range(1, len(prices)):
            price_today = prices[index]
            today_profit = price_today - min_price
            if today_profit > max_profit:
                max_profit = today_profit

            if price_today < min_price:
                min_price = price_today

        return max_profit
