import sys,os
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        sums=[[0 for j in range(length)] for i in range(length)]
        lower=0
        upper=length-1
        

    def optimal_sum(self, lower, upper, nums, opt_sums):
        if lower == upper:
            return nums[lower]
        else:
            opt_sums[lower][upper]=max(opt_sums[lower+1][upper-1], opt_sums[lower+1][upper-1]+nums[lower], opt_sums[lower+1][upper-1]+nums[upper], opt_sums[lower+1][upper-1]+nums[upper]+nums[lower])
            




        

my_solution = Solution()
print my_solution.myPow(2.94370 ,-9)
        
      