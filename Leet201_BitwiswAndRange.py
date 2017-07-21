"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = 0
        gap = n-m
        max_i = n
        min_i = m
        bits = [0 for _ in xrange(32)]
        for i in xrange(32):
            #take the i-th pos of max and min
            a =  max_i & 1
            b =  min_i & 1
            max_i >>= 1
            min_i >>= 1
            if a == 0 or b == 0:
                bits[i] = 0
            else:
                if gap >>i > 0:
                    bits[i] = 0
                else:
                    bits[i] = 1
        for each in bits[::-1]:
            ans |= each
            ans<<=1
        return ans