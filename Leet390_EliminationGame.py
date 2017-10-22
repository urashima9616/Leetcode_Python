class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = n
        gap = 1
        s = 1
        cnt = 1
        while L > 1:
            if cnt%2 != 0: # l->r
                if L%2 == 0:
                    s = s + 2*gap*(L/2 - 1) + gap
                else:
                    s = s + 2*gap*(L/2) - gap
            else:
                if L%2 == 0:
                    s = s - 2*gap*(L/2 - 1) - gap
                else:
                    s = s - 2*gap*(L/2) + gap
            gap *= 2
            cnt += 1
            L /=2
        return s
Solve =Solution()
print Solve.lastRemaining(13)

#1 2 3 4 5 6 7 8 9 10 11 12 13

#2 4 6 8 10 12

#2 6 10

#6
