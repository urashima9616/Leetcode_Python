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
            if each[0] == '':
                continue
            if each[0] == '.':
                moves = len(each)-1
                if moves == 0:
                    pass
                elif moves >0 and moves >= idx:
                    idx = 0
                elif moves >0 and moves < idx:
                    idx = idx - moves
            else:
                idx += 1
                if len(simpath)-1 <= idx:
                    simpath.append(each)
                else:
                    simpath[idx] = each
        return ''.join(simpath[0:idx+1])

Solve = Solution()
Solve.simplifyPath('//')