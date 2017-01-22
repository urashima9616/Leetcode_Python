import sys,os
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 2:
            return x*x
        if n == 1:
            return x
        if n == -2:
            return 1/x * 1/x
        if n == -1:
            return 1/x
        if n%2 != 0 and n > 0: # Odd number
            temp = self.myPow(x, (n-1)/2)
            return temp*temp*x
        elif n%2 == 0 and n > 0:
            temp = self.myPow(x, n/2)
            return temp*temp
        elif n%2 != 0 and n < 0: # Odd number
            temp = self.myPow(x, (n+1)/2)
            return temp*temp*1/x
        elif n%2 == 0 and n < 0:
            temp = self.myPow(x, n/2)
            return temp*temp

my_solution = Solution()
print my_solution.myPow(2.94370 ,-9)
        
      