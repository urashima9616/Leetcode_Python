import sys,os
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 0: 
            return False
        elif length == 1:
            return True
        index = nums[0]
        while index < length-1:
            if nums[index] == 0:
                return False
            index += nums[index]
        if index > length-1:
            return False
        else:
            return True
        

        

        
        
my_solution = Solution()
print my_solution.canJump([2,3,1,1,4])
        
      