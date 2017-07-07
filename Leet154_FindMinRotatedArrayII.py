"""
Duplicate entries allowed
this raises the complexity from log n to n/2 log n
key idea: 

if mid equal to two ends, there must be constant on
one side and min on the other.

if left end < mid < right: no rotation

if mid less than both ends => min on your left
if min greater than both ends => min on your right
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length ==1:
            return nums[0]
        elif length == 2:
            return nums[0] if nums[0]<=nums[1] else nums[1]
        else:
            mid = length/2
            right = 0
            if nums[mid] == nums[0] and nums[mid] == nums[-1]:#Need to search both direction
                prev = nums[mid]
                for i in xrange(mid,len(nums)):
                    if prev != nums[i]:
                        right = 1
                return self.findMin(nums[mid:]) if right == 1 else self.findMin(nums[:mid+1])
            elif nums[mid]>= nums[0] and nums[mid]<=nums[-1]: # no rotation
                return nums[0]
            elif nums[mid] >= nums[0] and nums[mid] >= nums[-1]:# on the right hand side
                return self.findMin(nums[mid:])
            elif nums[mid] <= nums[0] and nums[mid] <= nums[-1]: # on the left hand side
                return self.findMin(nums[:mid+1])