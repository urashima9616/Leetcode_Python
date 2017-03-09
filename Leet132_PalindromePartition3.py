"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

DFSearch solution
"""

class Solution(object):
    def partition(self, s):
        if not s:
            return []
        mincut = [len(s)]
        res = self.PalindromePart(s, 0, mincut)
        return mincut[0]
    def PalindromePart(self, s, k, mincut):
        if mincut[0] < k:
            return [[]]
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in xrange(len(s)):
            # check palindrom
            if s[:len(s)-i] == s[len(s)-i-1::-1]:
                if i > 0:
                    for each in self.PalindromePart(s[len(s)-i:], k+1, mincut):
                        res.append([s[:len(s)-i]] + each)
                        mincut[0] = k + len(each) if  mincut[0] > k + len(each) - 1 else mincut[0]
                else:
                    each = []
                    res.append([s[:len(s)-i]] + each)
                    mincut[0] = k + len(each) if  mincut[0] > k + len(each) - 1 else mincut[0]
        return res
Solve = Solution()
print Solve.partition('a')
