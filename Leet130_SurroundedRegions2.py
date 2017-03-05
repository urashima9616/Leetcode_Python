import Queue
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rowdim = len(board)
        coldim = len(board[0])
        openlist = Queue.Queue()
        for i in xrange(rowdim):
            for j in xrange(coldim):
                if board[i][j] == 'X' or board[i][j] == 'Y':
                    continue
                if (i == 0 and j == 0) or (i == rowdim-1 and j == coldim - 1):
                    board[i][j] = 'Y'
                    continue
                if i == rowdim- 1 or j == coldim -1 or i == 0 or j == 0: # boundary
                    if board[i][j] == 'O':
                        board[i][j] = 'Y'
                        openlist.put(self.getNeighbors(i, j, rowdim, coldim))
                        while not openlist.empty():
                            for each in openlist.get():
                                if not each:
                                    continue
                                if board[each[0]][each[1]] == 'O':
                                    board[each[0]][each[1]] = 'Y'
                                    openlist.put(self.getNeighbors(each[0], each[1], rowdim, coldim))
        for i in xrange(rowdim):
            for j in xrange(coldim):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


    def getNeighbors(self, row, col, rowdim, coldim):
        neighbors = [[row-1, col],[row+1, col],[row,col-1],[row, col+1]]
        if row == 0 and rowdim > 1:
            return [neighbors[1]]
        if row == rowdim -1:
            return [neighbors[0]]
        if col == 0 and coldim > 1:
            return [neighbors[3]]
        if col == coldim -1:
            return [neighbors[2]]
        return neighbors
Solve = Solution()
board = [['X','X','X','X'], ['X', 'O', 'O','X'], ['X','X','O','X'],['X','O','X','X']]
#board = ["X","O","X","X","OXOX","XOXO","OXOX","XOXO","OXOX"]
#board = [["O","X", "X","O","X"], ["X","O","O","X","O"], ["X","O","X","O","X"], ["O","X","O","O","O"],["X","X","O","X","O"]]
Solve.solve(board)
print "done"
