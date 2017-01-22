import sys,os
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_num = len(nums)
        if len_num == 0:
            return []
        if len_num == 1:
            return [nums]
        nums.sort()
        result = []
        result.append(nums)
        ii=0
        while self.next_permute(result[ii][:], len_num,result) == 0:
            ii += 1
        return result

    def next_permute(self, nums, len_num,result):
        for i in xrange(len_num):
            if i == 0:
                continue
            if nums[len_num-1-i] < nums[len_num-i]:
                index_swap=len_num-i
                for j in xrange(len_num-i, len_num):
                    if nums[j]<=nums[len_num-1-i]:
                        break
                    index_swap=j
                temp=nums[len_num-1-i]
                nums[len_num-1-i]=nums[index_swap]
                nums[index_swap]=temp
                temp_2=nums[len_num-i:]
                temp_2.reverse()
                result.append(nums[:len_num-i]+temp_2)
                return 0
        return 1 


my_solution = Solution()
print my_solution.permute([1, 2, 3])
        
      