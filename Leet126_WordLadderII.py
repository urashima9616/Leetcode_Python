"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        #Create pos-wise dictionary as candidate
        word_len = len(wordList[0])
        pos_dict = [{} for _ in xrange(word_len)]
        for each in wordList:
            for i in xrange(word_len):
                if each[i] not in pos_dict[i]:
                    pos_dict[i][each[i]] = 1
        res = []
        shortest_to_date={}
        shortest_to_date['s'] = 100000
        if(self.DFSearch([beginWord], beginWord, endWord, 1,pos_dict, shortest_to_date, res, wordList)):
            return res
        else:
            return []
        
                
        
    def DFSearch(self, path, current, target, level, pos_dict, shortest_to_date, res, wordList):
        if level > shortest_to_date['s']:
            return False
        if target == current:
            if path not in res:
                res.append(path)
                if len(path) <= shortest_to_date['s']:
                    shortest_to_date['s'] = len(path)
                return True
        for i in xrange(word_len):
            if target[i] == current[i]:
                continue
            if target[i] not in pos_dict[i]:
                return False
            temp = current[:i]+target[i]+current[i+1:]
            if temp in wordList:
                return self.DFSearch(path+[temp], temp, target, level+1, pos_dict, shortest_to_date, res, wordList)
            else:
                continue
        return False

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Solve = Solution()
Solve.findLadders(beginWord,endWord, wordList)