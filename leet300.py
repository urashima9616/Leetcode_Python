class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            opt_array = [1]
            for i in xrange(length):
                for j in xrange(i):
                    if opt_array[i]<opt_array[j]+1 and nums[i]>nums[j]:
                        opt_array[i] = opt_array[j]+1
mysolution = Solution()
print mysolution.lengthOfLIS([10,9,2,5,3,7,101,18])