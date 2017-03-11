class Solution():
    def DistinctPath(self, m, n):
        path = [[0 for i in xrange(m)] for j in xrange(n)]
        
        path[0][1] = 1
        path[1][0] = 1
        for i in xrange(1,m):
            for j in xrange(1,n):
                path[j][i] = path[j][i-1] + path[j-1][i]
        return path[n-1][m-1]
Solve = Solution()
print Solve.DistinctPath(3,4)