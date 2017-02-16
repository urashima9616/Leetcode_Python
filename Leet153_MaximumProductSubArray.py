class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        minsum = [0 for _ in xrange(numlen)]
        maxsum = [0 for _ in xrange(numlen)]
        minsum[0] = nums[0]
        maxsum[0] = nums[0]
        max_sum = nums[0]
        for i in xrange(1, numlen):
            minsum[i] = min(maxsum[i-1]*nums[i], minsum[i-1]*nums[i], nums[i])
            maxsum[i] = max(maxsum[i-1]*nums[i], minsum[i-1]*nums[i], nums[i])
            if max_sum < maxsum[i]:
                max_sum = maxsum[i]
        return max_sum