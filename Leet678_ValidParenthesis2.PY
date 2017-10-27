class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        cnt = 0
        for i in xrange(len(s)):
            if s[i] == "(" and cnt == 0:
                stack.append("(")
            elif s[i] == "(" and cnt != 0:
                while cnt > 0:
                    stack.append("*")
                    cnt -= 1
            elif s[i] == "*":
                stack.append("*")
            elif s[i] == ")":
                while len(stack) > 0 and stack[-1] == "*":
                    cnt += 1
                    stack.pop()
                else:
                    if len(stack) == 0:
                        cnt -= 1
                        if cnt < 0:
                            return False
                        continue
                    else:
                        stack.pop()
        if len(stack) > 0:
            while len(stack) > 0:
                if stack[-1] == "*":
                    cnt += 1
                    stack.pop()
                elif s[-1] == "(":
                    cnt -=1
                    if cnt < 0 :
                        return False
                    stack.pop()
            return True
        return True
Solve = Solution()
print Solve.checkValidString("*)(*")
