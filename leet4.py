"""
This is a solution set fot leetcode problems.
"""
import sys,os
class Solution():
    def convert(self, s, numRows):
        string_array=[ "" for i in range(numRows)]
        flag=0
        pt=0
        result_array=""
        for each in s:
            if numRows==1:
                string_array[0]+=each
                continue
            if numRows==2:
                string_array[pt]+=each
                pt+=1
                if pt==numRows:
                    pt=0
                continue
            if flag==0:
                string_array[pt]+=each
                pt+=1
                if pt==numRows:
                    flag=1
                    pt=numRows-2
                continue
            string_array[pt]+=each
            pt-=1
            if pt==0:
                flag=0
            continue
        for each in string_array:
            result_array+=each
        return result_array

my_sol=Solution()
print my_sol.convert("PAYPALISHIRING", 3)
