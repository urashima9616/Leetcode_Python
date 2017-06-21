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
        word_len = len(beginWord)
        word_count = len(wordList)
        pos_dict = [{} for _ in xrange(word_len)]
        for each in wordList:
            for i in xrange(word_len):
                if each[i] not in pos_dict[i]:
                    pos_dict[i][each[i]] = 1
        layer = [beginWord]
        visited = {}
        final = 0
        dist = 0
        res = []
        for i in xrange(word_count):
            next_layer = []
            for each_word in layer:
                #If the word has been branched at earlier levels, skip it
                if each_word in visited and visited[each_word] < i:
                    continue
                elif each_word not in visited:
                    visited[each_word] = i
                #If target is found at current layer, go no further 
                if each_word == target:
                    final = 1
                    dist = i
                    res.append(each_word)                 
                    continue
                elif final == 1: # if target already found at current layer, no expansion
                    continue
                else: # not yet find the target, do branching
                    for k in xrange(word_len):
                        if each_word[k] == target[k]:
                            continue
                        for literal in pos_dict[k]:
                            temp_word = each_word[:k]+literal+each_word[k+1:]
                            if temp_word not in wordList:
                                continue
                            next_layer.append(temp_word)
            if final == 1:
                break
            layer = next_layer
        return [res, dist]


Solve = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solve.findLadders(beginWord, endWord, wordList))


                