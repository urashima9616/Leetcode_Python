"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxprofit = 0
        minprice = prices[0]
        plen = len(prices)
        if plen == 1:
            return 0
        for i in xrange(1, plen):
            temp = prices[i] - minprice
            if temp > maxprofit:
                maxprofit = temp
                continue
            elif prices[i] < minprice:
                minprice = prices[i]
        return maxprofit