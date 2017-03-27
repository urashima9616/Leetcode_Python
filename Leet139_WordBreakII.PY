"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
Total Accepted: 82418
Total Submissions: 364560
Difficulty: Hard
Contributors: Admin
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #Make dictionary for the dict
        word = {}
        for _ in wordDict:
            word[_] = 1 if not word.has_key(_) else 1
        #Make the find_matrix
        find_matrix = [0 for _ in xrange(len(s))]
        
