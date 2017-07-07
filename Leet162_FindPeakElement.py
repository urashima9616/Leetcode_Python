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