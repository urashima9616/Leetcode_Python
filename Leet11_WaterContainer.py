class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        if len(height) == 2:
            return min(height[0], height[1])
        #Try two pointers
        start, end = [0, 1]
        max_water = 0
        max_idx = (0,0)
        while start<= end:
            #move end first
            while end < len(height)-1:
                cur_water = (end-start) * min(height[start], height[end])
                if cur_water > max_water:
                    max_water = cur_water
                    max_idx = (start, end)
                if  cur_water < (end-start +1) * min(height[start], height[end+1]):
                    end += 1
                else:
                    break
            while start < len(height) and start < end:
                cur_water = (end-start) * min(height[start], height[end])
                if cur_water > max_water:
                    max_water = cur_water
                    max_idx = (start, end)
                if  cur_water < (end-start -1) * min(height[start+1], height[end]):
                    start += 1
                else:
                    break
            if end < len(height)-1:
                end += 1
            else:
                if start < len(height):
                    start += 1
        return max_idx
Solve = Solution()
print Solve.maxArea([1,1,3,1,5,1,6,2,3])