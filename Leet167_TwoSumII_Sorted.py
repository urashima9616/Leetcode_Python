"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None
        num_dict = {}
        for i in xrange(len(numbers)):
            num_dict[numbers[i]] = i
        for i in xrange(len(numbers)):
            if numbers[i] > target:
                break
            if target-numbers[i] in num_dict:
                return [num_dict[target-numbers[i]]+1, i+1] if num_dict[target-numbers[i]] < i else [i+1, num_dict[target-numbers[i]]+1]