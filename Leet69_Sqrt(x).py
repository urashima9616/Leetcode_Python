"""
Implement int sqrt(int x).

Compute and return the square root of x.
Total Accepted: 130710
Total Submissions: 483545
Difficulty: Easy
Contributors: Admin
Newton method to find the cross-zero point of costfunction
f(g) = x - g*g
update rule 
g' = g + cost(g)/2*g

"""
from __future__ import division
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 1 or x == 0:
            return x
        #Take the initial guess
        ag = 1/2 * x
        costfunc = x- ag*ag
        while abs(costfunc) > 0.00000001:
            ag = ag + costfunc/(2*ag)
            costfunc = x- ag*ag
        return ag

Solve = Solution()
print Solve.mySqrt(2)