"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


The DP idea works like this:
let us say we know the optimal solution all the way to i-1 step
then here comes the i-th element, then the optimal solution for i-th step
must be obtained by following situations:
i-th element reaches back to certain elment j and construct a palindrome
the cut number is opt[j] + 1

then the optimal soution is the minimum of all possible such reaches.
that is to say, min(opt[j]+1) for all j<=i and P[i,j] == 1
<opt[j]<---------i
==================

#The calculation of P[i,j]
P[i,j] = P[i-1, j-1] if s[i] == s [j] else 0

P[i,i]=1
P[0, i] = s[:i] == s[i-1::-1]

You can change the min to sum
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        lens = len(s)
        #Set up the table
        pal_matrix = [ [ 0 for i in xrange(lens)] for j in xrange(lens)]
        pal_matrix[0][0] = 1
        for i in xrange(1,lens):
            pal_matrix[i][i] = 1
            if s[:i+1] == s[i::-1]:
                pal_matrix[0][i] = 1
        for i in xrange(1,lens):
            for j in xrange(i+1, lens):
                #pal_matrix[i][j] = pal_matrix[i][j-1] + pal_matrix[i-1][j]*pal_matrix[i-1][j-1] 
                #pal_matrix[i][j] = pal_matrix[i+1][j-1] if s[i] == s[j] else 0
                pal_matrix[i][j] = 1 if s[i:j+1] == s[j:i-1:-1] else 0
        opt_matrix = [0 for _ in xrange(lens)]
        for i in xrange(1, lens):
               opt_matrix[i] = min([opt_matrix[j-1] for j in xrange(i+1) if pal_matrix[j][i] == 1 ]) + 1 if not pal_matrix[0][i] else 0
        return opt_matrix[len(s)-1]

        
Solve = Solution()
print Solve.minCut("abcccc")


