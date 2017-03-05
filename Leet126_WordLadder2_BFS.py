"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

DFSearch solution
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not wordList:
            return None
        #set up hash table
        choice_pool = {}
        for each in wordList + [beginWord]:
            for other in wordList:
                if self.WordDist(each, other)  == 1:
                    if choice_pool.has_key(each):
                        choice_pool[each].append(other)
                    else:
                        choice_pool[each] = [other]
            if not choice_pool.has_key(each):
                choice_pool[each] = None
        res = []
        result = []
        minpath = [len(beginWord)]
        layer = [beginWord]
        parent_dict = {}
        finish = 1
        while layer and beginWord and finish:
            for each in layer:
                if each == endWord:
                    res.append(each)
                    finish = 0
                else:
                    for child in choice_pool[each]:
                        if not parent_dict.has_key(child):
                            parent_dict[child] = [each]
                        else:
                            parent_dict[child].append(each) 
            temp = [choice_pool[each] for each in layer if choice_pool[each]]
            layer = [group_member for group in temp for group_member in group]
        for each in res:
            path = [each]
            while parent_dict.has_key(each):
                path.append(parent_dict[each])
                each = parent_dict[each]
            path.reverse()
            result.append(path)
        return result
    def WordDist(self,s,t):
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return max(l1, l2)
        if s == t:
            return 0
        pt = 0
        count = 0
        while pt < l1 and count <2:
            if s[pt] != t[pt]:
                count += 1
            pt += 1
        return count
Solve = Solution()
print Solve.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        