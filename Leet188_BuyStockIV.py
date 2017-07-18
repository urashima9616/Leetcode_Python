class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        p_len = len(prices)
        max_profit = 0
        opt_matrix = [[0 for i in xrange(p_len)] for j in xrange(k+1)]
        for kk in xrange(1,k+1):
            prev_max = opt_matrix[kk-1][0]-prices[0]
            for i in xrange(1,p_len):
                opt_matrix[kk][i] = max(prices[i]+prev_max, opt_matrix[kk][i-1])
                prev_max = max(prev_max, opt_matrix[kk-1][i]-prices[i])
                max_profit = max(opt_matrix[kk][i], max_profit )
        return max_profit
Solve = Solution()

k = 2
prices = [4,51,2,3]
print Solve.maxProfit(k, prices)