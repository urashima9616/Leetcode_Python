"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Total Accepted: 139435
Total Submissions: 379156
Difficulty: Medium
Contributors: Admin
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        listlen = len(nums)
        if listlen == 0 or listlen == 1:
            return
        count = [0, 0, 0]
        i = j = k = 0
        for i in xrange(len(nums)):
            count[nums[i]] += 1
        i = 0
        if count[0] > 0:
            for i in xrange(count[0]):
                nums[i] = 0
            i += 1
        if count[1] > 0:
            for j in xrange(count[1]):
                nums[i+j] = 1
            j += 1
        if count[2] > 0:
            for k in xrange(count[2]):
                nums[i+j+k] = 2
Solve = Solution()
Solve.sortColors([1,1])