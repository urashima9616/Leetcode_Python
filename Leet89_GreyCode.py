"""
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        target = 2**n
        if target == 1:
            return [0]
        path = []
        res = [] 
        result = [0 for i in xrange(target)]
        path  = [0 for i in xrange(n)] 
        self.DFSearch(path, n, res, 0, target)
        #Merge the result
        for j in xrange(len(res)):
            for i in xrange(n):
                factor = 2**i
                result[j] += res[j][n-i-1]*factor
        return result
        
    def DFSearch(self, path, stop, res, k, target):
        if path in res:
            return
        res.append(path)
        k += 1
        if k == target:
            return
        for i in xrange(stop):
            flip = path[i]
            if flip == 0:
                flip = 1
            else:
                flip = 0
            if i == stop -1:
                self.DFSearch(path[:i] + [flip], stop, res, k, target)
            else:
                self.DFSearch(path[:i] + [flip] + path[i+1:], stop, res, k, target)
if __name__ == '__main__':
    Solve = Solution()
    Solve.grayCode(2)