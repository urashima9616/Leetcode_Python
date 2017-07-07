"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = 0
        for i in xrange(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if nums[i] != candidate:
                    count -= 1
                else:
                    count += 1
        count = 0
        for i in xrange(len(nums)):
            if nums[i] == candidate:
                count += 1
        if count > len(nums)/2:
            return candidate