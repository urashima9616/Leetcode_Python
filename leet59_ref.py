import sys,os
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0 :
            return []
        iter_num = n
        row_num = n
        col_num = n
        ele_num = n*n
        array_num = [ ele_num-i for i in xrange(ele_num) ]
        result = [[0 for i in xrange(n)] for j in xrange(n)]
        if iter_num%2 ==0:
            iter_num /= 2
        else: 
            iter_num = (iter_num+1)/2
        
        for i in xrange(iter_num):
            self.spiralWrite(i, row_num-1-i, i, col_num-1-i, result, array_num)
        return result

    def spiralWrite(self, row_i, row_e, col_i, col_e, result, array_num):
        col_len = col_e-col_i+1
        row_len = row_e-row_i+1
        if row_i == row_e and col_i == col_e:
            result[row_i][col_i] = array_num.pop()
            return
        for i in xrange(col_i, col_e+1):
            result[row_i][i] = array_num.pop()
        for i in xrange(row_i+1, row_e+1):
            result[i][col_e] = array_num.pop()
        for i in xrange(col_len-1):
            result[row_e][col_e-1-i] = array_num.pop()
        for i in xrange(row_len-2):
            result[row_e-1-i][col_i] = array_num.pop()
        
        
    

        
        
my_solution = Solution()
print my_solution.generateMatrix(1)
        
      