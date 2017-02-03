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
        listlen = xdim * ydim
        start = 0
        end = listlen-1
        while start<= end:
            mid = (start+end) // 2
            y_idx = mid // xdim
            x_idx = mid - y_idx*xdim
            if target < matrix[y_idx][x_idx]:
                 end = mid - 1
            elif target > matrix[y_idx][x_idx]:
                start = mid + 1
            else:
                return True
        return False



Solve = Solution()
print Solve.searchMatrix([[1,3]],3)