"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
Total Accepted: 152353
Total Submissions: 392901
Difficulty: Easy
Contributors: Admin

Two steps: a+b*2 = n
Step 1: for each a in range(0,n+1), find b
Sfep 2: for (a,b), calculate (a+b)!/a!b!
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        plans = []
        for a in xrange(n+1):
             if (n-a)%2 == 0:
                 plans.append([a,(n-a)/2])
        
        #sum up all the combinations
        result = 0
        for each in plans:
            if each[0] == 0 or each[1] == 0:
                result += 1
            else:# combinations = (a+b)!/(a! * b!)
                limit = max(each[0], each[1])
                div = min(each[0], each[1])
                temp = 1
                for i in xrange(limit+1, each[0]+1+each[1]):
                    temp *= i
                result += temp/self.factorial(div)
        return result
                    
    def factorial(self, n):
        if n == 0:
            return 1
        else: return n*self.factorial(n-1)