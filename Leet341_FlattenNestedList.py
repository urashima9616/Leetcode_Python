class Solution(object):
    def hasNext(self, nums):
        #type nums: List[List]
        #rtype : List[int]
        res = []

        def VisitList(nums):
            for each in nums:
                if isinstance(each, list):
                    VisitList(each)
                else:
                    res.append(each)
            return
        VisitList(nums)
        for each in res:
            yield each


Solve = Solution()
for each in Solve.hasNext([1,2,3,[4,5]]):
    print each