"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
Total Accepted: 65099
Total Submissions: 269440
Difficulty: Hard
Contributors: Admin

Idea: uphills always start with 1
      downhill always end with 1 
      to make the required candies minimal
      So scan from left to right to have uphills 1, 2, 3, 4...
      then scan again from right to left to have uphills(downhills) 1,2,3,4
      return max(candy1, candy2)
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        lens = len(ratings)
        if lens == 0 or lens == 1:
            return 1
        candy1 = [1 for _ in xrange(lens)]
        candy2 = [1 for _ in xrange(lens)]
        for i in xrange(1, lens):
            if ratings[i] > ratings[i-1]:
                candy1[i] = candy1[i-1] + 1
            if ratings[lens-i-1] > ratings[lens-i]:
                candy2[lens-i-1] = candy2[lens-i] + 1
        for i in xrange(lens):
            candy1[i] = max(candy1[i], candy2[i])
        return sum(candy1)
Solve = Solution()
Solve.candy([2,1])