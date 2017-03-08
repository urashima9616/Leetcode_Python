"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        if not s:
            return []
        res = self.PalindromePart(s)
        return res
    def PalindromePart(self, s):
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in xrange(1, len(s)+1):
            # check palindrom
            if s[:i] == s[i-1::-1]:
                for each in self.PalindromePart(s[i:]):
                    res.append([s[:i]] + each)
        return res
                