import sys, os

class Solution():
    def lengthOfLongestSubstring(self, s):
        str_len = len(s)
        if str_len==0:
            return 0
        pt_i = 0
        pt_e = 0
        alpha_beta={}
        max_len=1
        for pt_e in xrange(str_len):
            print pt_e
            if alpha_beta.has_key(s[pt_e]):
                temp_len=pt_e-pt_i
                if(max_len<temp_len):
                    max_len=temp_len
                #Update dictionary
                for pt_i in xrange(pt_i,alpha_beta[s[pt_e]]):
                    del alpha_beta[s[pt_i]]
                #Update pt_i to alpha_beta[s[pt_e]]+1
                pt_i=alpha_beta[s[pt_e]]+1
                alpha_beta[s[pt_e]]=pt_e
                continue
            if pt_e==str_len-1:
                temp_len=pt_e-pt_i+1
                if(max_len<temp_len):
                    max_len=temp_len
                return max_len
            alpha_beta[s[pt_e]]=pt_e
        return max_len

my_sol=Solution()
print my_sol.lengthOfLongestSubstring("dvdf")
print "hello world"
