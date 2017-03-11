class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        lens = len(ratings)
        candy1 = [0 for _ in xrange(lens)]
        candy2 = [0 for _ in xrange(lens)]
        nums = [i+1 for i in xrange(lens)]
        if  lens == 1:
            return 1
        hills = []
        direct = 0
        #first round, collect the uphills and downhills
        if ratings[0] > ratings[1]:
            direct = -1
        elif ratings[0] < ratings[1]:
            direct = 1
        else:
            direct = 0
        start = 0
        for i in xrange(1,lens):
            #if ratings[i] == ratings[i-1]:
            #    continue
            if ratings[i] < ratings[i-1] and direct == 1: # plateu or downhill
                hills.append([start, i-1, direct])
                start = i-1
                direct = -1
                continue
            if ratings[i] == ratings[i-1] and direct == 1:
                hills.append([start, i-1, direct])
                start = i-1
                direct = 0
                continue
            if ratings[i] > ratings[i-1] and direct == -1:
                hills.append([start, i-1, direct])
                start = i-1
                direct = 1
                continue
            if ratings[i] == ratings[i-1] and direct == -1:
                hills.append([start, i-1, direct])
                start = i-1
                direct = 0
                continue
            if ratings[i] != ratings[i-1] and direct == 0:
                hills.append([start, i-1, direct])
                start = i-1
                direct = 1 if ratings[i] > ratings[i-1] else -1
        hills.append([start, lens-1, direct])
        for each in hills:
            if each[2] == 1:
                candy1[each[0]:each[1]+1] = nums[:each[1]-each[0]+1]
            if each[2] == -1:
                candy2[each[0]:each[1]+1] = nums[each[1]-each[0]-1::-1]
        for i in xrange(lens):
            candy1[i] = 1 if candy1[i] == 0 and candy2[i] == 0 else max(candy1[i], candy2[i])
        return sum(candy1)

        
Solve = Solution()
print Solve.candy([1,1,3,4,5,1,1,0])