"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 1:
            return True
        pt1 = 0
        pt2 = len(s)-1
        while pt1 < len(s) and pt2 > 0:
            if not s[pt1].isalnum() and not s[pt2].isalnum():
                pt1 += 1
                pt2 -=1
            elif not s[pt1].isalnum():
                pt1 += 1
            elif not s[pt2].isalnum():
                pt2 -= 1
            else:
                if s[pt1].lower() != s[pt2].lower():
                    return False
                else:
                    pt1 += 1
                    pt2 -= 1
        return True