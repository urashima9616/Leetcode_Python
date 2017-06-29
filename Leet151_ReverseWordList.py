class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return ""
        word_array = s.split(" ")
        res =""
        for each in word_array[::-1]:
            if each:
                res = res+ each + " "
        return res[:len(res)-1]
s = "the sky is blue"
Solve = Solution()
print Solve.reverseWords(s)