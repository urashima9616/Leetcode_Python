"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
Total Accepted: 108350
Total Submissions: 425225
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ydim = len(board)
        if ydim == 0:
            return False
        xdim = len(board[0])
        if xdim == 0:
            return False
        wordlen = len(word)
        if wordlen == 0:
            return False
        if ydim*xdim < wordlen:
            return False
        path = []
        wordlist = list(word)
        for i in xrange(ydim):
            for j in xrange(xdim):
                path = []
                if board[i][j] == wordlist[0]:
                    if self.DFSearch(board, j, i, j, i, xdim, ydim, path, wordlist, wordlen, 0):
                        return True
        return False
        
        
    def DFSearch(self, choice_pool, xprev, yprev, xstart, ystart, xdim, ydim, path, target, k, layer):
        if choice_pool[ystart][xstart] != target[layer]:
            return False
        k -= 1
        layer += 1
        
        if k == 0 and path + [choice_pool[ystart][xstart]] == target:
            return True
        elif k == 0:
            return False
        #Search adjacent cells
        right, left, up, down = (False, False, False, False)
        if xstart < xdim -1 and (xstart+1, ystart) != (xprev,yprev): #Move right
            right = self.DFSearch(choice_pool, xstart, ystart, xstart+1, ystart, xdim, ydim, path + [choice_pool[ystart][xstart]], target, k, layer)
        if xstart > 0 and (xstart-1, ystart) != (xprev,yprev): #Move left
            left  = self.DFSearch(choice_pool, xstart, ystart, xstart-1, ystart, xdim, ydim, path + [choice_pool[ystart][xstart]], target, k, layer)
        if ystart > 0 and (xstart, ystart-1) != (xprev,yprev): #Move up
            up = self.DFSearch(choice_pool, xstart, ystart, xstart, ystart-1, xdim, ydim, path + [choice_pool[ystart][xstart]], target, k, layer)
        if ystart < ydim-1 and (xstart, ystart+1) != (xprev,yprev): #Move down
            down = self.DFSearch(choice_pool, xstart, ystart, xstart, ystart+1, xdim, ydim, path + [choice_pool[ystart][xstart]], target, k, layer)
        for each in (right, left, up, down):
            if each == True:
                return True
        return False
if __name__ == '__main__':
    Solve = Solution()
    board = ["aaa","abb","abb","bbb","bbb","aaa","bbb","abb","aab","aba"]


    print Solve.exist(board, "aabaaaabbb")
