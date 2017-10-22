import Queue
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        accum = [0 for _ in xrange(len(nums))]
        accum[0] = nums[0]
        for i in xrange(1,len(nums)):
            accum[i] = accum[i-1] + nums[i]
        cnt = m-1
        min_heap = Queue.PriorityQueue()
        #(1-sum, i, j)
        min_heap.put((1-accum[len(nums)-1], 0, len(nums)-1))

        while cnt > 0:
            seg = min_heap.get()
            min_sum = 1-seg[0]
            i, j = seg[1], seg[2]
            if i == j:
                return min_sum
            for k in xrange(i,j):
                if k == i == 0:
                    temp = max(nums[k], accum[j]-accum[k])
                else:
                    if i > 0:
                        temp = max(accum[k]-accum[i-1], accum[j]-accum[k]) 
                    else:
                        temp = max(accum[k], accum[j]-accum[k])
                if min_sum > temp:
                    min_sum = temp
                    cut = k
            seg_sum1 = accum[cut] - accum[i-1] if i > 0 else accum[cut]
            seg_sum2 = accum[j] - accum[cut]
            seg1 = (1-seg_sum1, i, cut)
            seg2 = (1-seg_sum2, cut+1, j)
            min_heap.put(seg1)
            min_heap.put(seg2)
            cnt -= 1
        seg = min_heap.get()
        return 1-seg[0]
Solve = Solution()
print Solve.splitArray([7,2,5,10,8], 1)






