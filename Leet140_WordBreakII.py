"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

Key idea:

remember the different choices (partition index, word) to partition at index i
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        s_len = len(s)
        wordDict = set(wordDict)
        opt_vec = [[] for _ in xrange(s_len)]
        valid_vec = [0 for _ in xrange(s_len)]
        res = []
        for i in xrange(s_len):
            if s[:i+1] in wordDict:
                opt_vec[i].append((-1, s[:i+1]))
                valid_vec[i] = 1
            for j in xrange(i):
                if valid_vec[j]== 1 and s[j+1:i+1] in wordDict:
                    opt_vec[i].append((j,s[j+1:i+1]))
                    valid_vec[i] = 1
        if not valid_vec[-1]:
            return []
        self.ConstructPath(-1, opt_vec, res, "")
        return res
            

    def ConstructPath(self, index, opt_vec, res, path):
        for each in opt_vec[index]:
            if each[0] == -1:
                if path == '':
                    res.append(each[1])
                else:
                    res.append(each[1] + " "+ path[:-1])
            else:
                self.ConstructPath(each[0], opt_vec, res, each[1]+ " " + path)
        return

        
Solve = Solution()
s = "a"
wordDict = ["a"]
print Solve.wordBreak(s,wordDict)

        



