"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

Key idea: DP solution. 
"""



class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """        
        num_row = len(dungeon)
        num_col = len(dungeon[0])
        if not num_col or not num_row:
            return None
        opt_matrix = [[0 for i in xrange(num_col)] for j in xrange(num_row)]
        opt_matrix[num_row-1][num_col-1] = -dungeon[num_row-1][num_col-1]+1 if -dungeon[num_row-1][num_col-1]+1 >1 else 1
        for i in xrange(num_row):
            for j in xrange(num_col):
                if i==j==0:
                    continue
                row_id, col_id = num_row-1-i, num_col-1-j
                if row_id == num_row-1:
                    opt_matrix[row_id][col_id] = opt_matrix[row_id][col_id+1]-dungeon[row_id][col_id]
                elif col_id == num_col-1:
                    opt_matrix[row_id][col_id] = opt_matrix[row_id+1][col_id]-dungeon[row_id][col_id]
                else:
                    opt_matrix[row_id][col_id] = min(opt_matrix[row_id+1][col_id], opt_matrix[row_id][col_id+1])-dungeon[row_id][col_id]
                if opt_matrix[row_id][col_id] < 1:
                    opt_matrix[row_id][col_id] = 1
        return opt_matrix[0][0]