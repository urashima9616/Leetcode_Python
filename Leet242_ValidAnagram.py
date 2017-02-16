class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1_len = len(s)
        s2_len = len(t)
        letter_dict = {}
        count  = 0
        if s1_len != s2_len:
            return False
        for each in s:
            if letter_dict.has_key(each):
                letter_dict[each] += 1
            else:
                letter_dict[each] = 1
        for each in t:
            if not letter_dict.has_key(each):
                return False
            else:
                letter_dict[each] -= 1
        for key, val in letter_dict.items():
            if val != 0:
                return False
        return True
Solve = Solution()
Solve.isAnagram('anagram','nagaram')
