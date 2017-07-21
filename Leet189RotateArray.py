class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        shifts = k%num_len if k > num_len else k
        copy = nums[num_len-shifts:num_len]
        nums[shifts:num_len] = nums[:num_len-shifts] 
        nums[:shifts] = copy
    def rotate2(self, nums, k):
        pass

