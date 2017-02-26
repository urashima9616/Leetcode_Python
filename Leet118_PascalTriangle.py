"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        for i in xrange(numRows):
            for j in xrange(i+1):
                if j == 0:
                    temp = [1]
                elif j == i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1] + res[i-1][j])
            res.append(temp)
        return res