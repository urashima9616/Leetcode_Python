class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def bsearch(array, target):
            start, end = 0, len(array)-1
            while start<= end:
                mid = (start+end)/2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    end = mid -1
                elif array[mid] > target:
                    start = mid + 1
            return start
        nums = []
        while n !=0:
            nums.append(n%10)
            n /= 10
        n = nums[::-1]
        
        for i in reversed(xrange(len(n))):
            if i == len(n)-1:
                continue
            if n[i+1] > n[i]: # first descending pos
                #search the pos to swap
                reversed_temp = n[i+1:][::-1]
                #idx = bsearch(reversed_temp, n[i])
                idx = 0
                while reversed_temp[idx] <= n[i]:
                    idx += 1
                swapee = reversed_temp[idx]
                reversed_temp[idx] = n[i]
                n = n[:i] + [swapee] + reversed_temp
                return n
        return -1
Solve = Solution()
Solve.nextGreaterElement(12443322)
9199999999