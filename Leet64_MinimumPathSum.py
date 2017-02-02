"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
Total Accepted: 98873
Total Submissions: 264970
Difficulty: Medium
Contributors: Admin
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ydim = len(grid) 
        if ydim == 0:
            return 0
        xdim = len(grid[0])
        
        mincost = [[0 for i in xrange(xdim)] for j in xrange(ydim) ] 
        mincost[0][0] = grid[0][0]
        for i in xrange(1, xdim):
            mincost[i][0] = mincost[i-1][0] + grid[i][0]
        for j in xrange(1, ydim):
            mincost[0][j] = mincost[0][j-1] + grid[0][j]
        for i in xrange(1, xdim):
            for j in xrange(1, ydim):
                mincost[i][j] = min(mincost[i-1][j], mincost[i][j-1])
        #Trace back to get the path
        path = [[xdim-1, ydim-1]]
        i, j = (xdim-1, ydim-1)
        while i!= 0 and j!=0:
            if mincost[i-1][j] <= mincost[i][j-1]:
                path.append([i-1,j])
                i -= 1
            else:
                path.append([i,j-1])
                j-=1
            #path.append([i-1,j]) if mincost[i-1][j] <= mincost[i][j-1] else path.append([i,j-1])
        return mincost[xdim-1][ydim-1]

if __name__ == '__main__':
    Solve = Solution()
    Solve.minPathSum([[0]])