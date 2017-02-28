class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        state 0 : has 1st stock
        state 1:  finish 1st stock
        state 2:  has 2nd stock
        state 3:  finish 2nd stock
        """
        if not prices or len(prices) ==1 :
            return 0
        opt = [[0 for i in xrange(len(prices))] for j in xrange(4)]
        opt[0][0] = -prices[0]
        opt[1][0] = 'invalid'
        opt[2][0] = 'invalid'
        opt[3][0] = 0
        for i in xrange(1, len(prices)):
            opt[0][i] = max(opt[0][i-1], -prices[i])
            opt[1][i] = max(opt[1][i-1], opt[0][i-1]+prices[i]) if opt[1][i-1] != 'invalid' else opt[0][i-1]+prices[i]
            if opt[1][i-1] != 'invalid':
                opt[2][i] = max(opt[2][i-1], opt[1][i-1]-prices[i], opt[1][i]-prices[i]) if opt[2][i-1] != 'invalid' else max(opt[1][i-1]-prices[i], opt[1][i]-prices[i])
            elif opt[1][i-1] == 'invalid':
                opt[2][i] = 'invalid'
            opt[3][i] = opt[2][i-1] + prices[i] if opt[2][i-1] != 'invalid' else 0
        return max(opt[0][len(prices)-1], opt[1][len(prices)-1], opt[2][len(prices)-1], opt[3][len(prices)-1])
Solve = Solution()
print Solve.maxProfit([1, 3, 2, 4, 6])