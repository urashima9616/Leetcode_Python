#DP solution
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        opt = [[0 for i in xrange(len(s))] for j in xrange(len(s))]
        cnt = 0
        for i in xrange(len(opt)):
            opt[i][i] = 1
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    opt[i][i+1] = 1
        
        
        for i in xrange(len(opt)):
             # fill opt for case where (i-j)%2 = 0
            k = i
            j = i
            cnt += opt[i][j]
            while(k > 0 and j < len(s)-1):
                opt[k-1][j+1] = opt[k][j] if s[k-1] == s[j+1] else 0
                cnt += opt[k-1][j+1]
                k -= 1
                j += 1
            k = i
             # fill opt for case where (i-j)%2 = 1
            if k< len(s)-1 and opt[k][k+1] == 1:
                j = k+1
                cnt += opt[k][j]
                while(k > 0 and j < len(s)-1):
                    opt[k-1][j+1] = opt[k][j] if s[k-1] == s[j+1] else 0
                    cnt += opt[k-1][j+1]
                    k -= 1
                    j += 1
                    
        return cnt
Solve = Solution()
print Solve.countSubstrings("aaaaa")




            
