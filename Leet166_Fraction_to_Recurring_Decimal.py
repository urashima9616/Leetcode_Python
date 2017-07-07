"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.

"""



class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator:
            return None
        div_set = {}
        if numerator == 0:
            return "0"
        #sign decision
        if numerator * denominator > 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
            sign = ""
        else:
            numerator = abs(numerator)
            denominator = abs(denominator)
            sign = "-"
        
        inter_part = numerator/denominator
        res = numerator%denominator
        if res == 0:
            return sign+str(inter_part)
        frac = []
        count = 0
        while(res not in div_set and res != 0):
            div_set[res] = count
            result = str(res*10/denominator)
            frac.append(result)
            res = res*10%denominator
            count +=1
        if res == 0:
            outcome = sign + "".join(str(inter_part)+"."+"".join(frac))
        else:
            outcome = sign + "".join(str(inter_part)) + '.' + "".join(frac[:div_set[res]]) + "("+ "".join(frac[div_set[res]:]) + ")"
        return outcome
Solve = Solution()
print Solve.fractionToDecimal(1,123)
