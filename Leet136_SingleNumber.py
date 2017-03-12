"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#In-place solution takes XOR for all entries in the list. The remaining result is the number to find
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diction = {}
        for each in nums:
            if not diction.has_key(each):
                diction[each] = 1
            else:
                del diction[each]
        key, val = diction.items()[0]
        return key
Solve = Solution()
Solve.singleNumber([1])