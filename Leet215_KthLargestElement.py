class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        k_inv = len(nums)-k+1
        if k_inv > len(nums):
            return None

        def findKRecursive(start, end):
            if start == end:
                return nums[start]
            pivot_index = pivoting(start, end)
            if pivot_index == k_inv-1:
                return nums[pivot_index]
            else:
                return findKRecursive(start, pivot_index-1) if pivot_index > k_inv-1 else findKRecursive(pivot_index+1,end)
        def pivoting(start,end):
            pivot = nums[end]
            i = start - 1
            for j in xrange(start, end):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            if nums[i+1] > pivot: #if equal, no need to swap
                nums[i+1], nums[end] = nums[end], nums[i+1]
            return i+1
        
        return findKRecursive(0, len(nums)-1)

Solve = Solution()
print Solve.findKthLargest([5,2,4,1,3,6,0],4)