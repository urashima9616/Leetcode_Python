import sys,os
class Solution(object):
    def swap_Sort(self, index, nums, result, n):
        if nums == 0:
            return
        trial, i = [0, 1]
        while 1:
            if index+i >= n:
                return
            if result[index+i] > result[index]:
                trial += 1
                if trial == nums:
                    temp = result[index]
                    result[index] = result[index+i]
                    result[index+i] = temp
                    temp_array = result[index+1:]
                    temp_array.sort()
                    result[index+1:] = temp_array
                    break
            i += 1 
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        if n == 0: 
            return ""
        if n == 1:
            return "1"
        if n == k:
            for i in xrange(n):
                res = res + str(n-i)
            return res
        if k == 1:
            for i in xrange(n):
                res = res + str(i+1)
            return res
        k = k-1
        digit_array = [ 1 for i in xrange(n-1)]
        k_index = -1
        for i in xrange(n-2):
            digit_array[i+1]=(i+2)*digit_array[i]
        temp = k
        permute_array = []
        result =[]
        for i in xrange(n-1):
            result.append(i+1)
            div = temp/digit_array[n-2-i]
            permute_array.append(div)
            temp = temp%digit_array[n-2-i]
        result.append(n)
        for i in xrange(len(permute_array)):
            self.swap_Sort(i, permute_array[i], result, n)
        for i in xrange(n):
                res = res+str(result[i])
        return res
my_solution = Solution()
print my_solution.getPermutation(3,3)
        
      