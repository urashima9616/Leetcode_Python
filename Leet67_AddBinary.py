"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Total Accepted: 123252
Total Submissions: 401710
Difficulty: Easy
Contributors: Admin
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len1 = len(a)
        len2 = len(b)
        if len1 == 0:
            return b
        elif len2 == 0:
            return a
        lenmax = max(len1, len2)
        carry = 0
        result = []
        for i in range(lenmax):
            idx1 = len1-1-i
            idx2 = len2-1-i
            if idx1 < 0:
                temp = int(b[idx2]) + carry
            elif idx2 < 0:
                temp = int(a[idx1]) + carry
            else:
                temp = int(b[idx2]) + int(a[idx1]) + carry
            
            if temp == 1:
                carry = 0
                result.append('1')
            elif temp == 2:
                carry = 1
                result.append('0')
            elif temp == 3:
                carry = 1
                result.append('1')
            elif temp == 0:
                result.append('0')
                carry = 0
        
        if carry == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)