"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

[leet, leetc, ode]
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        worddict = {}
        for each in wordDict:
            worddict[each] = 1
        possible = [0 for _ in xrange(len(s))]
        possible[0] = worddict[s[0]] if worddict.has_key(s[0]) else 0
        for i in xrange(1,len(s)):
            if worddict.has_key(s[:i+1]):
                possible[i] = 1
            else:
                for k in xrange(i):
                    if possible[k] and worddict.has_key(s[k+1:i+1]):
                        possible[i] = 1
                        break
        return True if possible[len(s)-1] else False

