class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_len = len(nums)
        lprd, rprd = ([0 for _ in xrange(num_len)], [0 for i in xrange(num_len)])
        if not nums:
            return []
        for i in xrange(num_len):
            if i == 0:
                lprd[i] = nums[i]
                rprd[num_len-i-1] = nums[num_len-i-1] 
            else:
                lprd[i] = lprd[i-1]*nums[i]
                rprd[num_len-i-1] = nums[num_len-i-1]*rprd[num_len-i]
        res = [0 for _ in xrange(num_len)]
        for i in xrange(num_len):
            if i == 0:
                res[i] = rprd[1]
            elif i == num_len - 1:
                res[i] = lprd[num_len-2]
            else:
                res[i] = lprd[i-1] * rprd[i+1]
        return res