import sys,os
class Solution():
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len=len(s)
        work_stack=[0 for i in range(str_len)]
        count_L=0
        count_R=0
        count=0
        top_pt=0
        pen_pt=0
        max_count=0
        for each in s:
            if each==')':
                count_R+=1
            elif each=='(':
                count_L+=1
            if count_R>count_L:
                if max_count<count*2:
                    max_count=count*2
                #Discard the invalid parenthesis
                continue
            if work_stack[pen_pt]=='(' and each==')':
                count_R-=1
                count_L-=1
                count+=1
                top_pt=pen_pt
                if pen_pt>0:
                    pen_pt=pen_pt-1
                else:
                    pen_pt=0
                continue
            work_stack[top_pt]=each
            pen_pt=top_pt
            top_pt+=1
        if count*2>max_count:
            max_count=count*2
        
        return max_count

my_sol=Solution()
print my_sol.longestValidParentheses("()(())")
