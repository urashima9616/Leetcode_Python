class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #opt[i][j] = opt[i-1][j-1] if s[i-1] == p [i-1] or p[i-1] == "?"
        #if p[i-1] == "*" and it represents empty sequence, opt[i][j] = opt[i][j-1]
        # if p[i-1] == "*" and it represents repeating some characters opt[i][j] = opt[i-1][j]
        #opt[0][0] = False
        opt = [[False for i in xrange(len(p)+1)] for j in xrange(len(s)+1)]
        opt[0][0] = True
        for i in xrange(1,len(s)+1):
            opt[i][0] = False
        for i in xrange(len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] != "*":
                    opt[i][j] = (i > 0) and opt[i-1][j-1] and ( s[i-1] == p[j-1] or p[i-1] == "?")
                else:
                    opt[i][j] = (i > 0) and (opt[i][j-1] or opt[i-1][j])
        return opt[len(s)][len(p)]
Solve = Solution()
print Solve.isMatch("abefcdgiescdfimde", "ab*cd?i*de")