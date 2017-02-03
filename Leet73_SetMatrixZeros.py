"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Total Accepted: 90425
Total Submissions: 256788
Difficulty: Medium
Contributors: Admin
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #First pass, change the non-zero to 'z'
        ydim = len(matrix)
        if ydim == 0:
            return
        xdim = len(matrix[0])
        for i in xrange(ydim):
            for j in xrange(xdim):
                if matrix[i][j] == 'z':
                    continue
                if matrix[i][j] == 0: #M:ark the elements in row, col as 'z'
                    for k in xrange(xdim):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'z'
                    for k in xrange(ydim):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'z'
        #Second pass, change 'z' to 0
        for i in xrange(ydim):
            for j in xrange(xdim):
                if matrix[i][j] == 'z':
                    matrix[i][j] = 0

