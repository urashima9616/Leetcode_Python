class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        sums = [0 for _ in xrange(numlen)]
        sums[0] = nums[0]
        maxsum = sums[0]
        for i in xrange(1, numlen):
            sums[i] = max(sums[i-1]+nums[i], nums[i])
            if sums[i] > maxsum:
                maxsum = sums[i]
        return maxsum