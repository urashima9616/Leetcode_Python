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
            twos = (cur_two ^ each) & (cur_one)
        return ones