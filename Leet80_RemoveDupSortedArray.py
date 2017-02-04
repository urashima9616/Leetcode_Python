"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length.
Total Accepted: 103643
Total Submissions: 296057
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        if numlen == 0:
            return 0
        if numlen == 1:
            return 1
        slow_pt  = 0
        fast_pt = 0
        count = 0
        count_global = 0
        wr_pt = 0
        while fast_pt < numlen:
            if nums[fast_pt] == nums[slow_pt]:
                count += 1
            else:
                if count >= 2:
                    count_global += 2
                    count = 1
                else:
                    count_global += count
                    count = 1
                slow_pt = fast_pt
            if count <3:
                    nums[wr_pt] = nums[fast_pt]
                    wr_pt += 1
            fast_pt += 1
        if count >= 2:
            count_global += 2
        else:
            count_global += count
        return count_global
if __name__ == '__main__':
    Solve = Solution()
    print Solve.removeDuplicates([1,1,1,2,2,3])