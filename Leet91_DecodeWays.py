"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
Total Accepted: 103492
Total Submissions: 545953
Difficulty: Medium
Contributors: Admin
DP
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlen = len(s)
        if strlen == 0:
            return 0
        if strlen == 1 and s[0] != '0':
            return 1
        if s[0] == '0':
            return 0
            
        num = [0 for i in xrange(strlen)]
        num[0] = 1
        if int(s[0:2]) >26 and s[1] == '0':
            return 0
        elif int(s[0:2]) > 26 and s[1] != '0':
            num[1] = 1
        elif int(s[0:2]) <= 26 and s[1] == '0':
            num[1] = 1
        elif int(s[0:2]) <=26 and s[1] != '0':
            num[1] = 2
    
        for i in xrange(2,strlen):
            if s[i] == '0' and  s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                num[i] = num[i-2]
            elif s[i] == '0' and  s[i-1] == '0':
                return 0
            elif s[i] == '0' and int(s[i-1:i+1]) > 26:
                return 0
            elif s[i] != '0' and s[i-1] == '0':
                num[i] = num[i-1] 
            elif  s[i] != '0' and int(s[i-1:i+1]) <= 26:
                num[i] = num[i-1] + num[i-2]
            elif s[i] !=0 and int(s[i-1:i+1]) > 26:
                num[i] = num[i-1] 
    
        return num[strlen-1]

Solve = Solution()
print Solve.numDecodings('1234')
