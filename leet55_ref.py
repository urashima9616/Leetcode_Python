import sys,os
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        row_num = len(matrix)
        if row_num == 0:
            return result
        col_num = len(matrix[0])
        iter_num = min(col_num, row_num)
        if iter_num%2 ==0:
            iter_num /= 2
        else: 
            iter_num = (iter_num+1)/2
        
        for i in xrange(iter_num):
            self.spiralVisit(i, row_num-1-i, i, col_num-1-i, matrix, result)
        return result
    def spiralVisit(self,row_i, row_e, col_i, col_e, matrix, result):
        col_len = col_e-col_i+1
        row_len = row_e-row_i+1
        if row_i == row_e and col_i == col_e:
            result.append(matrix[row_i][col_i])
            return
        if row_len == 1:
            result.extend(matrix[row_i][col_i:col_e+1])
            return 
        if col_len == 1:
            for i in xrange(row_i, row_e+1):
                result.append(matrix[i][col_i])
            return 
        result.extend(matrix[row_i][col_i:col_e+1])
        
        for i in xrange(row_i+1, row_e+1):
            result.append(matrix[i][col_e])
        for i in xrange(col_len-1):
            result.append(matrix[row_e][col_e-1-i])
        for i in xrange(row_len-2):
            result.append(matrix[row_e-1-i][col_i])
        
    

        
        
my_solution = Solution()
print my_solution.spiralOrder([[7],[9],[6]])
        
      