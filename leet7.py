import sys,os
class Solution():
    def reverse(self, x):
        sign=1
        if x<0:
            sign=-1
            x=x*-1
        token=str(x)
        str_rev=""
        str_len=len(token)
        for i in range(str_len):
            str_rev+=token[str_len-i-1]
        num_rev=int(str_rev)
        if sign==1 and num_rev>2**31-1:
            return 0
        if sign==-1 and num_rev>2**31:
            return 0
        return num_rev*sign

my_sol=Solution()
print my_sol.reverse(123)
