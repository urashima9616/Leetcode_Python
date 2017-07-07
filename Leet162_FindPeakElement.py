"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


Key idea:
 binary search, check the triplet consists of the element in the middle 
 (mid-1, mid, mid+1) (mid, mid+1, mid+2)

 
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        return self.findit(nums, 0, len(nums)-1)
                
    def findit(self, nums, head, tail):
        if len(nums[head:tail+1]) < 3:
            return None
        if len(nums[head:tail+1]) == 3:
            if nums[head+1]>nums[head] and nums[head+1]>nums[tail]:
                return head+1
            else:
                return None
        mid = (head+tail)/2
        if nums[mid] > nums[mid-1] and nums[mid]> nums[mid+1]:
            return mid
        elif nums[mid+1] > nums[mid] and nums[mid+1]> nums[mid+2]:
            return mid+1
        else:
            return self.findit(nums, head, mid) or self.findit(nums, mid+1, tail)