class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        choice = set([int(each) for each in time if each.isdigit()])
        cand = sorted(list(choice))
        pos_dict = {}
        for i in xrange(len(cand)):
            pos_dict[cand[i]] = i 
            
        def isValid(time):
            hour, minute = time.split(":")
            if int(hour) > 24 or int(minute) > 60:
                return False
            return True
            
        for i in reversed(xrange(len(time))):
            if time[i] == ":":
                continue
            next_idx = pos_dict[int(time[i])]+1
            
            if next_idx >= len(cand):
                time = time[:i] + str(cand[0]) + time[i+1:]
            else:
                new_time = time[:i] + str(cand[next_idx]) + time[i+1:]
                if isValid(new_time):
                    time = new_time
                    break
                else:
                    time = time[:i] + str(cand[0]) + time[i+1:]
        return time
Solve = Solution()
print Solve.nextClosestTime("19:39")