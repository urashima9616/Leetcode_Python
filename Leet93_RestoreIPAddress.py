"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
Total Accepted: 75405
Total Submissions: 289693
Difficulty: Medium
Contributors: Admin
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strlen = len(s)
        if strlen < 4:
            return []
        path = []
        res = []
        choice_pool = list(s)
        self.DFSearch(choice_pool, 0, path, res, 3)
        result = []
        for each in res:
            result.append(''.join(each))
        return result
        
    def DFSearch(self, choice_pool, start, path, res, k):
        if k == 0:
            if len(choice_pool[start:]) >= 4: # No more than 4 digits
                return
            if len(choice_pool[start:]) == 3 and int(''.join(choice_pool[start:])) > 255:
                return
            if len(choice_pool[start:]) > 1 and choice_pool[start] == '0':
                return  
            path = path + choice_pool[start:]
            res.append(path)
            return
        if start >= len(choice_pool)-1:
            return
        if len(choice_pool[start:])-1 < k: # The remaining # of literals -1 is less than remaining dots...
            return
        for i in xrange(start, start+3): #No more than 3 digits
            if i >= len(choice_pool)-1:
                break
            if i > start and  choice_pool[start] == '0':
                break
            if int(''.join(choice_pool[start:i+1])) > 255:
                break
            
            self.DFSearch(choice_pool, i+1, path+choice_pool[start:i+1]+['.'], res, k-1)
if __name__ == "__main__":
    Solve = Solution()
    print Solve.restoreIpAddresses("010010")