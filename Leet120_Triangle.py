"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        tlen = len(triangle)
        if not tlen:
            return None
        
        op_matrix = [[0 for i in xrange(tlen)] for j in xrange(tlen)] 
        op_matrix[0][0] = triangle[0][0]
        for i in xrange(1, tlen):
            for j in xrange(i+1):
                if i == j:
                    op_matrix[i][j] = op_matrix[i-1][j-1] + triangle[i][j]
                elif j == 0:
                    op_matrix[i][j] = op_matrix[i-1][j] + triangle[i][j]
                #elif i -j < 2 :
                #    op_matrix[i][j] = min(op_matrix[i-1][j], op_matrix[i-1][j-1]) + triangle[i][j]
                else:
                    op_matrix[i][j] = min(op_matrix[i-1][j-1], op_matrix[i-1][j]) + triangle[i][j]
        return min(op_matrix[tlen-1])
Solve = Solution()
Solve.minimumTotal([ [2], [3,4], [6,5,7], [4,1,8,3]])