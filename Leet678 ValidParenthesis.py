"Naive Solution"
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkParenthesis(s):
            a = []
            for each in s:
                if each == "(":
                    a.append(each)
                elif each == ")":
                    if len(s) == 0:
                        return False
                    else:
                        a.pop()
                elif each == "":
                    continue
                else:
                    return False
            return True
        
        def searchAssign(i, path):
            if i == len(star):
                assign.append(path)
                return
            for symbol in ("(", ")", "s"):
                searchAssign(i+1, path + symbol)
        
        star = []
        symbols = list(s)
        if checkParenthesis(symbols):
            return True

        for i in xrange(len(symbols)):
            if symbols[i] == "*":
                star.append(i)
        assign = []
        searchAssign(0, "")
        for each in assign:
            new_symbols = symbols
            i = 0
            for k in star:
                new_symbols[k] = each[i] if each != "s" else ""
                i += 1
            if checkParenthesis(new_symbols):
                return True
Solve = Solution()
print Solve.checkValidString("(*)")