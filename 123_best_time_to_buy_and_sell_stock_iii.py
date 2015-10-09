"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    """
    Idea:
        find a day 'i' to separate two transactions and find the max,
        since you have to sell then you can buy again.
            --> max_profit = max(maxBy[i] + maxSince[i]), at day i
        so two matrixes, one scans forward, one scans backward and use DP to find max.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if prices == None or len(prices) < 2:
            return max_profit

        maxBy = [0 for i in range(len(prices))]
        maxSince = [0 for i in range(len(prices))]
        valley = prices[0]
        peak = prices[-1]

        # build maxBy
        for i in range(1, len(prices)):
            maxBy[i] = max(maxBy[i-1], prices[i] - valley)
            valley = min(valley, prices[i])

        # build maxSince & find max_profit
        for i in reversed(range(len(prices)-1)):
            maxSince[i] = max(maxSince[i+1], peak - prices[i])
            peak = max(peak, prices[i])
            max_profit = max(max_profit, maxBy[i] + maxSince[i])

        return max_profit
