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
        path = []
        res = []
        minpath = [len(beginWord)]
        
        self.DFSearch(choice_pool, beginWord, path, 0, res, minpath, endWord)
        return [[beginWord] + each for each in res if len(each) == minpath[0]]
        
    def DFSearch(self, choice_pool, root, path, k, res, minpath, target):
        if root == target:
            if path[:k] not in res:
                res.append(path[:k])
                if k < minpath[0]:
                    minpath[0] = k
            return
        if k > minpath[0]:
            return
        if not choice_pool.has_key(root):
            return
        for each in choice_pool[root]:
             if each not in path[:k]:
                if len(path) == k:
                    path.append(each)
                else:
                    path[k] = each
                self.DFSearch(choice_pool, each, path, k+1, res, minpath, target)

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
print Solve.findLadders("hot", "dog", ["hit", "dit", "dig", "dog", "hog"])
            
        