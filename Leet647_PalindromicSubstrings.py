class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValid(s):
            return s == s[::-1]
        cnt = 0
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s)+1):
                cnt = cnt + 1 if isValid(s[i:j]) else cnt
        return cnt
Solve = Solution()
print Solve.countSubstrings("abc")
