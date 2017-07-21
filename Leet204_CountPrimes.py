"""
Description:

Count the number of prime numbers less than a non-negative number, n.
key idea: 
Sieve of Eratosthenes
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n==1:
            return 0
        if n==2:
            return 0
        if n == 3:
            return 1
        upper = int(n**(0.5))
        nums = n-2
        primes = [1 for _ in xrange(n+1) ]
        for i in xrange(2,upper+1):
            if primes[i]:
                base = i*i
                index = (n-1-base)/i
                for j in xrange(index+1):
                    if not primes[j*i+base]:
                        continue
                    primes[j*i+base] = 0
                    nums -=1
        return nums
Solve = Solution()
print Solve.countPrimes(18)