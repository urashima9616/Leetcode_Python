"""
No duplicate allowed

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
            if nums[mid] >= nums[0] and nums[mid] >= nums[-1]:# on the right hand side
                return self.findMin(nums[mid:])
            elif nums[mid] <= nums[0] and nums[mid] <= nums[-1]: # on the left hand side
                return self.findMin(nums[:mid+1])
            elif nums[mid]>= nums[0] and nums[mid]<=nums[-1]: # no rotation
                return nums[0]