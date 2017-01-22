import sys,os
class Solution():
    def maxArea(self, height):
        length=len(height)
        start=0
        end=length-1
        max_val=0
        temp_val=0
        #Dynamical programming method
        while(end>start):
            if height[start]>height[end]:
                temp_val=height[end]*(end-start)
                if temp_val>max_val:
                    max_val=temp_val
                end-=1
            elif height[start]<height[end]:
                temp_val=height[start]*(end-start)
                if temp_val>max_val:
                    max_val=temp_val
                start+=1
            else:
                temp_val=height[start]*(end-start)
                if temp_val>max_val:
                    max_val=temp_val
                start+=1
                end-=1    
        return max_val

test_str='abc'
test_str_2='abc'
test=test_str^test_str_2
print test

my_sol=Solution()
print my_sol.maxArea([1,3,2,5,25,24,5])
