import sys,os
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        if m== 0 and n== 0:
            return 0
        temp_result=1
        iter_num = m+n-2
        m_fact = 0
        n_fact = 0
        for i in xrange(m+n-2):
            temp_result = temp_result*(i+1)
            if i == m-2:
                m_fact = temp_result
            if i == n-2: 
                n_fact = temp_result
        return temp_result/(m_fact*n_fact)
my_solution = Solution()
print my_solution.uniquePaths(2,2)
        
      