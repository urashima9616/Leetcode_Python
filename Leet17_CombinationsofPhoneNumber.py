class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #make dictionary
        digits2letter = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        if not digits:
            return res
        def makewords(i, path):
            if i > len(digits)-1:
                res.append(path)
                return
            else:
                for each in digits2letter[digits[i]]:
                    makewords(i+1, path + each)
            return
        makewords(0, "")
        return res
