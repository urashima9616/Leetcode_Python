class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #MinMax structure
        def getmin(nums, path):
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 3:
                path += str(nums[0]) + "/"  +str(nums[1]) + "/" + str(nums[2]) 
                return nums[0]/(nums[1]*nums[2])
            else:
                return nums[0]/getmax(nums[1:], path)
        def getmax(nums, path):
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 3:
                path += str(nums[0]) + "/" + "(" + str(nums[1]) + "/" + str(nums[2]) + ")"
                return nums[0]*nums[2]/nums[1]
            else:
                path += str(nums[0]) + "/" + "("
                return nums[0]/getmin(nums[1:], path)
        path = ""
        max_div = getmax(nums, path)
        return path
Solve = Solution()
Solve.optimalDivision([100,1100,10,2])