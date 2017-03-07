class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        res = self.GetPalindrome(s)
        return res
    def GetPalindrome(self, s):
        if len(s) == 1:
            return [[s]]
        res = []
        if self.CheckPalindrome(s):
            res.append([s])
        for i in xrange(1,len(s)):
            left = s[:i]
            right = s[i:]
            lplist = self.GetPalindrome(left)
            rplist = self.GetPalindrome(right)
            for l in lplist:
                for r in rplist:
                    can = l +r
                    if can not in res:
                        res.append(l+r)
        return res
            
    def CheckPalindrome(self, s):
        if len(s) == 1:
            return True
        pt1 = 0
        pt2 = len(s) -1
        #Assume all letters assert(s[pt1].isalphanumeric())
        while pt1 <= pt2:
            if s[pt1] != s[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
        return True
Solve = Solution()
print Solve.partition("aabc")