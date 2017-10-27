class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos_dict = {}
        pt_0, pt_1 = [0] * 2
        max_len = 0
        while pt_1 < len(s):
            if s[pt_1] not in pos_dict:
                pos_dict[s[pt_1]] = pt_1
            else:
                if max_len < pt_1 - pt_0:
                    max_len = pt_1 - pt_0
                    pt_0 = pos_dict[s[pt_1]] + 1
                    pos_dict[s[pt_1]] = pt_1
            pt_1 +=1
        return max_len
Solve = Solution()
print Solve.lengthOfLongestSubstring("abcabcbb")