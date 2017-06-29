class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
        operators = set(("+", "-", "*", "/"))
        stack = []
        for each in tokens:
            if each not in operators:
                stack.append(int(each))
            elif each in operators:
                op1, op2 = stack.pop(), stack.pop()
                if each == "*":
                    res = op2 * op1
                elif each == "+":
                    res = op2 + op1
                elif each == "-":
                    res = op2- op1
                else:
                    res = int(float(op2*1.0/op1))
                stack.append(res)
        return int(stack.pop())

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Solve = Solution()
print Solve.evalRPN(tokens)