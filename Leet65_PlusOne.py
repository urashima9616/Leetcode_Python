"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
Total Accepted: 147550
Total Submissions: 397739
Difficulty: Easy
Contributors: Admin
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digitlen = len (digits)
        carry = 1
        result =[]
        for i in xrange(digitlen):
            if carry == 1:
                temp = carry + digits[digitlen-1-i]
                if temp > 9:
                    carry = 1
                    result.append(temp-10)
                else:
                    carry = 0
                    result.append(temp)
            else:
                result.append(digits[digitlen-1-i])
        if carry > 0:
            result.append(carry)
            
        result.reverse()
        return result

Solve = Solution()
print Solve.plusOne([0])