import sys,os
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        opt_sums=[0 for i in xrange(length)]
        return self.optimal(length-1, nums, opt_sums)
        

    def optimal(self, upper, nums, opt_sums):
        if upper == 0:
            return nums[upper]
        else:
            opt_sums[upper-1]=self.optimal(upper-1, nums, opt_sums)
            res= max(opt_sums[upper-1], nums[upper])
            return res

        
        
my_solution = Solution()
print my_solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        
      