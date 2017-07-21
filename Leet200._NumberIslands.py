'''
Leetcode 200:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded 
by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Idea to solve: Transfer the map into a adjacency matrix, each row corresponds to a land in the map
Then run BFS to connect the connected component
Start with one node and record all nodes that can be reached. 
Then pick one node outside my record and run it again until working set is empty
the number of iterations is the number of islands.
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0
        count = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for i in xrange(cols)] for j in xrange(rows)]
        for i in xrange(rows):
            for j in xrange(cols):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                self.DFSearch(i, j, grid, visited)
                count += 1
        return count
    
    def DFSearch(self, row, col, grid, visited):
        visited[row][col] = 1
        rows, cols = len(grid), len(grid[0])
        #search up
        if row != 0 and not visited[row-1][col] and grid[row-1][col]=='1':
            self.DFSearch(row-1, col, grid, visited)
        #search down
        if row != rows-1 and not visited[row+1][col] and grid[row+1][col]=='1':
            self.DFSearch(row+1, col, grid, visited)
        #search left
        if col!= 0 and not visited[row][col-1] and grid[row][col-1]=='1':
            self.DFSearch(row, col-1, grid, visited)
        #search right
        if col != cols-1 and not visited[row][col+1] and grid[row][col+1]=='1':
            self.DFSearch(row,col+1, grid,visited)
        return
Solve = Solution()
grid = ["11000","11010","00100","00011"]
print Solve.numIslands(grid)