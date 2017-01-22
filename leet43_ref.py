import sys,os
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_1=len(num1)
        len_2=len(num2)
        len_3=len_1+len_2
        res=[0 for each in range(len_3)]
        result=[]
        if num1 == '0' or num2 == '0':
            return '0'
        for x1_index in xrange(len_1):
            digit_1=int(num1[-1-x1_index])
            base=x1_index
            carry_prev=0
            for x_2_index in xrange(len_2):
                digit_2=int(num2[-1-x_2_index])
                sum_temp=carry_prev+digit_1*digit_2
                partial_sum=sum_temp%10
                carry=(sum_temp-partial_sum)/10
                partial_sum_res=res[base+x_2_index]+partial_sum
                res[base+x_2_index]=partial_sum_res%10
                carry_2=(partial_sum_res-res[base+x_2_index])/10
                carry_prev=carry+carry_2
            res[base+len_2]=res[base+len_2]+carry_prev     
        if res[-1]==0:
            for i in range(len_3-1):
                result.append(str(res[-2-i]))
        else:
            for i in range(len_3):
                result.append(str(res[-1-i]))
                
        res_2 = ''.join(str(e) for e in result)
        return res_2
            


        
my_solution = Solution()
print my_solution.multiply('9','9')
        
      