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
        for i in xrange(rowdim):
            for j in xrange(coldim):
                if board[i][j] == 'X':
                    continue
                elif i == rowdim- 1 or j == coldim -1 or i == 0 or j == 0:
                    continue
                else:
                    path = []
                    if self.DFSearchX(i, j, path, board, rowdim, coldim):
                        for (row, col) in path:
                            board[row][col] = 'X'
    def DFSearchX(self, row, col, path, board, rowdim, coldim):
        if row == rowdim - 1 or col == coldim -1 or row == 0 or col == 0: #boundary node
            return False
        up = down = right = left = True
        path.append([row, col])
        #down
        if [row+1, col] not in path:
            down = True if board[row+1][col] == 'X' else self.DFSearchX(row+1, col, path, board, rowdim, coldim)
        if not down:
            return False
        #up
        if [row-1, col] not in path:
            up = True if board[row-1][col] == 'X' else self.DFSearchX(row-1, col, path, board, rowdim, coldim)
        if not up:
            return False
        #left
        if [row, col-1] not in path:
            left = True if board[row][col-1] == 'X' else self.DFSearchX(row, col-1, path, board, rowdim, coldim)
        if not left:
            return False
        #right
        if [row, col+1] not in path:
            right = True if board[row][col+1] == 'X' else self.DFSearchX(row, col+1, path, board, rowdim, coldim)
        if not right:
            return False
        if up and down and right and left:
            return True
        else:
            return False
Solve = Solution()
#board = [['X','X','X','X'], ['X', 'O', 'O','X'], ['X','X','O','X'],['X','O','X','X']]
#board = ["X","O","X","X","OXOX","XOXO","OXOX","XOXO","OXOX"]
board = [["O","X", "X","O","X"], ["X","O","O","X","O"], ["X","O","X","O","X"], ["O","X","O","O","O"],["X","X","O","X","O"]]
"""
 ["OXXOX",
  "XXXXO",
  "XXXXX",
  "OXOOO",
  "XXOXO"]

  ["OXXOX",
   "XXXXO",
   "XXXOX",
   "OXOOO",
   "XXOXO"]
"""
Solve.solve(board)
print "done!" 