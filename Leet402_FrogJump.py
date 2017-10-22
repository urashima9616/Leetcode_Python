class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return False
        opt = [{} for _ in xrange(len(stones))]
        opt[0][1] = 1
        for i in xrange(1,len(stones)):
            for j in reversed(xrange(0,i)):
                if stones[i] - stones[j] > i+1: # greater than the possible biggest jump
                    break
                if len(opt[j]) == 0:
                    continue
                if (stones[i] - stones[j]) in opt[j]:
                    opt[i][stones[i] - stones[j]] = 1
                    opt[i][stones[i] - stones[j] + 1] = 1
                    if  stones[i] - stones[j] > 1:
                        opt[i][stones[i] - stones[j]-1] = 1
            
        return len(opt[len(stones)-1]) > 0