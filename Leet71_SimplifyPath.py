"""
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Total Accepted: 74502
Total Submissions: 308795
Difficulty: Medium
Contributors: Admin
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        strlen = len(path)
        if strlen == 1:
            return "/"
        simpath = ["/"]
        path_element = path.split('/')
        idx = 0
        for each in path_element:
            if each == '':
                continue
            if each[0]  == '.':
                moves = len(each)-1
                if moves == 0:
                    pass
                elif moves >0 and moves >= idx:
                    idx = 0
                elif moves >0 and moves < idx:
                    idx = idx - moves
            else:
                if idx == len(simpath) - 1:
                    simpath.append(each)
                    idx += 1
                elif idx < len(simpath) - 1:
                    simpath[idx+1] = each
                    idx += 1
        result = '/'.join(simpath[0:idx+1])
        return result[1:]

Solve = Solution()
print Solve.simplifyPath('/a/./b/../../c/')