"""
Key Idea:

"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return False
        if t < 0 or k <= 0:
            return False
            
        dict_k = {}
        for i in xrange(len(nums)):
            if t > 0:
                if i>=k+1:
                    dict_k.pop(nums[i-k-1]/t)
                val1, val2, val3 = dict_k.get(nums[i]/t), dict_k.get(nums[i]/t-1), dict_k.get(nums[i]/t+1)
                if val1 is None:
                    dict_k[nums[i]/t] = nums[i]
                if val1 is not None:
                    if abs(val1-nums[i])<=t:
                        return True
                if val2 is not None:
                    if abs(val2-nums[i])<=t:
                        return True
                if val3 is not None:
                    if abs(val3-nums[i])<=t:
                        return True  
            else:
                if i>=k+1:
                    dict_k.pop(nums[i-k-1])
                val = dict_k.get(nums[i])
                if val is not None:
                    return True
                else:
                    dict_k[nums[i]] = nums[i]
        return False
Solve = Solution()
Solve.containsNearbyAlmostDuplicate([3,6,0,2], 2, 2)