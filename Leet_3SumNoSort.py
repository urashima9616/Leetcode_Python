import Queue
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        quick_hash = {}
        queues = Queue.PriorityQueue()
        for i in xrange(len(nums)):
            if -(nums[i]) not in quick_hash:
                quick_hash[-nums[i]] = [i]
            else:
                quick_hash[-nums[i]].append(i)
        res = set([])
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] in quick_hash:
                    for each in quick_hash[nums[i] + nums[j]]:
                        if each != i and each != j:
                            queues.put(nums[i])
                            queues.put(nums[j])
                            queues.put(-(nums[i]+nums[j]))
                            temp = ""
                            while not queues.empty():
                                temp += str(queues.get())
                            res.add(temp)
                            break 
        return res
Solve = Solution()
print Solve.threeSum([-1,0,1,2,-1,-4])