# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        def binaryinsert(intervals, target):
            start, end = 0, len(intervals)-1
            while start<= end:
                mid = (start+end)/2
                if target == intervals[mid][0]:
                    return mid
                elif target  > intervals[mid][0]:
                    start = mid + 1
                elif target < intervals[mid][0]:
                    end = mid -1
            return start
        idx = binaryinsert(intervals, newInterval[0])
        #check left
        left = 0
        if idx > 0:
            if newInterval[0] <= intervals[idx-1][1]:
                left = 1
        #check right:
        pre, pre_abut, mid = [0] * 3
        idx_right = -1
        for i in xrange(idx, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                pre = 1
                idx_right = i
                break
            if newInterval[1] == intervals[i][0]:
                pre_abut = 1
                idx_right = i
                break
            
            if newInterval[1] <= intervals[i][1]:
                mid = 1
                idx_right = i
                break
        #Merge
        if left:
            if pre:
                return intervals[:i-1] + [[intervals[idx-1][0], newInterval[1]]] + intervals[right_idx:]
            if pre_abut or mid:
                return intervals[:i-1] + [[intervals[idx-1][0], intervals[right_idx][1]]] + intervals[right_idx+1:]      
        else:
            if pre:
                return intervals[:i] + [[newInterval[0], newInterval[1]]] + intervals[right_idx:]
            if pre_abut or mid:
                return intervals[:i] + [[newInterval[0], intervals[right_idx][1]]] + intervals[right_idx+1:]