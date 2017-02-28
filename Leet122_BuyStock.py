"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
#Dynamic programming
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        opt_matrix = [[0 for i in xrange(len(prices))] for j in xrange(2)]
        opt_matrix[0][0] = 0
        opt_matrix[1][0] = -prices[0]
        max_gain = 0
        for i in xrange(1, len(prices)):
            opt_matrix[0][i] = max(opt_matrix[1][i-1]+prices[i], opt_matrix[0][i-1])
            opt_matrix[1][i] = max(opt_matrix[0][i-1] - prices[i], opt_matrix[1][i-1])
            max_temp = max(opt_matrix[0][i], opt_matrix[1][i])
            max_gain = max_temp if max_temp > max_gain else max_gain
        return max_gain