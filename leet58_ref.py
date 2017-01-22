import sys,os
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
       # last_symbol=s[-1]
       # if last_symbol == ' ':
       #     return 0
       # else:
        string_array = s.split()
        return len(string_array[-1])
        
        

        

        
        
my_solution = Solution()
print my_solution.lengthOfLastWord("       ")
        
      