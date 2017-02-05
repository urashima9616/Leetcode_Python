"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
Total Accepted: 83532
Total Submissions: 253804
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        numslen = len(nums)
        if numslen == 0:
            return False
        return self.BinarySearch(nums, 0, numslen-1, target)
        
    def BinarySearch(self, search_pool, start, stop, target):
        #Base test
        if start > stop:
            return False
        #Step 1: Get the mid
        mid = (start+stop)//2
        if search_pool[mid] == target:
            return True
        #Check the right side
        while search_pool[mid] == search_pool[stop] and stop >= mid:
            stop -= 1
        if stop < mid: 
            return self.BinarySearch(search_pool, start, mid-1, target)
            
        if search_pool[mid] < search_pool[stop]: # right side sorted
            if target > search_pool[mid]:
                right = self.BinarySearch(search_pool, mid+1, stop, target)
                if not right:
                     left = self.BinarySearch(search_pool, start, mid-1, target)
                return right or left
            else:
                return self.BinarySearch(search_pool, start, mid-1, target)
        else:#left side is sorted
            if target < search_pool[mid]:
                left = self.BinarySearch(search_pool, start, mid-1, target)
                if not left:
                    right = self.BinarySearch(search_pool, mid+1, stop, target)
                return left or right
            else:
                return self.BinarySearch(search_pool, mid+1, stop, target)

Solve = Solution()
print Solve.search([1], 2)