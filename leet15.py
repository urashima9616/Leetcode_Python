import sys,os
class Solution():
    def threeSum(self, nums):
        nums.sort()
        result=[]
        result_hash_array=[]
        length=len(nums)
        pt=0
        if length<3:
            return result
        for iter in range(length-2):
            if iter>0:
                if nums[iter-1]==nums[iter]:
                    continue
            start=iter+1
            end=length-1
            while(start<end):
                if start>iter+1 and nums[start-1]==nums[start]:
                    start+=1
                    continue
                if end<length-1 and nums[end+1]==nums[end]:
                    end-=1
                    continue
                sum=nums[iter]+nums[start]+nums[end]
                if sum==0:
                    result.append([nums[iter],nums[start],nums[end]])
                    start+=1
                    end-=1
                elif sum>0:
                    end-=1
                elif sum<0:
                    start+=1
            
        return result

my_sol=Solution()
print my_sol.threeSum([-1,0,1,2,-1,-4])
