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
        visited = set(beginWord)
        shortest_to_date={}
        shortest_to_date['s'] = 100000
        if(self.DFSearch([beginWord], beginWord, endWord, 1, pos_dict, shortest_to_date, res, wordList,visited)):
            return [each for each in res if len(each)==shortest_to_date['s']]
        else:
            return []
        
    def DFSearch(self, path, current, target, level, pos_dict, shortest_to_date, res, wordList, visited):
        if level > shortest_to_date['s']:
            return False
        if target == current:
            if path not in res:
                res.append(path)
                if len(path) <= shortest_to_date['s']:
                    shortest_to_date['s'] = len(path)
                return True
        flag = False
        for i in xrange(len(target)):
            if target[i] == current[i]:
                continue
            if target[i] not in pos_dict[i]:
                return False
            for each in pos_dict[i].keys():
                temp = current[:i]+each+current[i+1:]
                if temp in wordList and temp not in visited:
                    #visited.add(temp)
                    flag = flag | self.DFSearch(path+[temp], temp, target, level+1, pos_dict, shortest_to_date, res, wordList, visited)
                else:
                    continue
        return flag

#beginWord = "qa"
#endWord = "sq"
#wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Solve = Solution()
print(Solve.findLadders(beginWord,endWord, wordList))