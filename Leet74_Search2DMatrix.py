"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Total Accepted: 109504
Total Submissions: 308289
Difficulty: Medium
Contributors: Admin
Binary search, pay attention to the condition start <= end
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ydim = len(matrix)
        if ydim == 0:
            return False
        xdim = len(matrix[0])
        if xdim == 0:
            return False
        #Binary row search first
        start = 0
        end = ydim-1
        while start <= end:
            mid = (start + end) //2
            if target  > matrix[mid][0]:
                start = mid+1
            elif target == matrix[mid][0]:
                return True
            else:
                end = mid -1
        if end < 0 : return False
        idx_col = end
        #Binary col search
        start = 0
        end = xdim-1
        while start <= end:
            mid = (start+end)//2
            if target == matrix[idx_col][mid]:
                return True
            elif target < matrix[idx_col][mid]:
                end = mid -1
            elif target > matrix[idx_col][mid]:
                start = mid + 1
        return False


Solve = Solution()
print Solve.searchMatrix([[1,3]],3)