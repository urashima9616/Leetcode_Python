"""
00 
0, 1, 0, 1, 0, 1,
0, 1, 1, 0, 0, 0,  ones
0, 0, 0, 1, 1, 0,  twos
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0
        for each in nums:
            cur_one = ones
            cur_two = twos
            ones = (cur_one ^ each) & (~cur_two)
            twos = (cur_two ^ each) & (cur_one) | (~cur_one)&(~each)&cur_two
        return ones
Solve = Solution()
Solve.singleNumber([0,1,0,1,0,1,2]) 