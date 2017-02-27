class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in xrange(numRows+1):
            for j in xrange(i+1):
                if j == 0:
                    temp = [1]
                elif j == i:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1] + res[i-1][j])
            res.append(temp)
        return res[numRows]
        