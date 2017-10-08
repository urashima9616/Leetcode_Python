class Solution(object):
    def findMajorElement3(self, nums):
        """
        :type nums: List[int]

        """
        if not nums:
            return None
        c1, c2 = 0, 0
        n1, n2 = 0, 0
        cand = {}
        for each in nums:
            if each == n1:
                c1 += 1
            elif each == n2:
                c2 += 1
            elif c1 == 0:
                c1, n1 = 1, each
            elif c2 == 0:
                c2, n2 = 1, each
            else:
                c1, c2 = c1 - 1, c2 - 1
        cnt1, cnt2 = 0, 0
        for each in nums:
            if c1 > 0 and each == n1:
                cnt1 += 1
            if c2 > 0 and each == n2:
                cnt2 += 1
        if cnt1 > len(nums)/3 :
            return n1
        if cnt2 > len(nums)/3 :
            return n2
        return None
Solve = Solution()
print Solve.findMajorElement3([1,3,1,3,3,4,1,3,1])         
                

