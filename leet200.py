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