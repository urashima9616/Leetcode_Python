class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0 or length == 1:
            return 0
        if length == 2:
            return max(prices[1]-prices[0], 0)
        max_profit = -1*max(prices)
        profit_matrix = [[0 for i in xrange(4)] for i in xrange(length+1)]
        profit_matrix[0][2] = -prices[0]
        profit_matrix[0][3] = max_profit
        
        for i in xrange(1,length):
            for j in xrange(1,4):
                if j == 1:
                    profit_matrix[i][j] = max(profit_matrix[i-1][1], profit_matrix[i-1][3])
                if j == 2:
                    profit_matrix[i][j] = max(profit_matrix[i-1][1]-prices[i-1], profit_matrix[i-1][2])
                if j == 3:
                    profit_matrix[i][j] = profit_matrix[i-1][2]+prices[i-1]
                
                if max_profit <= profit_matrix[i][j]:
                    max_profit = profit_matrix[i][j]
        return max(profit_matrix[length][1], profit_matrix[length][3])

        
                    
                        
                    
        

mysolution = Solution()
print mysolution.maxProfit([1, 2, 4])