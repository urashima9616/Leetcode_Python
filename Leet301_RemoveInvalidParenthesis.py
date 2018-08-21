class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [s]
        #function return # of left, right mismatches
        def misCount(s):
            left, right = 0, 0
            for each in s:
                if each == "(":
                    left += 1
                elif each == ")" and left > 0:
                    left -= 1
                elif each == ")" and left == 0:
                    right += 1
            return (left, right)
        l, r = misCount(s)
        root = [(s,l,r)]
        final = 0
        res = []
        explored = set([])
        while not final:
            next_root = []
            for each in root:
                l_tmp, r_tmp = each[1:]
                explored.add(each[0])
                if l_tmp > 0 and r_tmp > 0:
                    for i in xrange(len(each[0])):
                        if each[0][i] not in ("(", ")"):
                            continue
                        if each[0][i] == "(" or each[0][i] == ")":
                            tmp = each[0][:i]+each[0][i+1:]
                            if tmp in explored:
                                continue
                            l, r = misCount(tmp)
                            if l+r < l_tmp + r_tmp:
                                next_root.append((tmp, l, r))
                elif l_tmp > 0 and r_tmp == 0:
                    for i in xrange(len(each[0])):
                        if each[0][i] == "(":
                            tmp = each[0][:i]+each[0][i+1:]
                            if tmp in explored:
                                continue
                            l, r = misCount(tmp)
                            if l+r < l_tmp + r_tmp:
                                next_root.append((tmp, l, r))
                elif l_tmp == 0 and r_tmp > 0:
                    for i in xrange(len(each[0])):
                        if each[0][i] == ")":
                            tmp = each[0][:i]+each[0][i+1:]
                            if tmp in explored:
                                continue
                            l, r = misCount(tmp)
                            if l+r < l_tmp + r_tmp:
                                next_root.append((tmp, l, r))
                else:#found the valid solution
                    final = 1
                    res.append(each[0])
            root = next_root
        
        return [each for each in set(res)]
Solve = Solution()
Solve.removeInvalidParentheses(")(())((((()(")