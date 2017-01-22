import sys,os
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        dim=len(matrix)
        if dim == 0:
            return
        residual = dim%2
        if residual == 0:
            index_ub = dim/2
        else:
            index_ub = (dim-1)/2
        #Mirror it against the diagnal
        for i in xrange(dim):
            for j in xrange(i+1,dim):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in xrange(dim):
            for j in xrange(index_ub):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][dim-1-j]
                matrix[i][dim-1-j]=temp
        return matrix


my_solution = Solution()
print my_solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
        
      