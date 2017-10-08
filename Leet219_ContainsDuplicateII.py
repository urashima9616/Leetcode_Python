class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup_set = {}
        if not nums:
            return False
        for i in xrange(len(nums)):
            dupidx = dup_set.get(nums[i])
            if dupidx is None:
                dup_set[nums[i]] = i
            else:
                diff = i-dupidx
                if diff <= k:
                    return True
                else:
                    dup_set[nums[i]] = i
                    
        return False
Solve = Solution()
print Solve.containsNearbyDuplicate([-1,-1],1)
