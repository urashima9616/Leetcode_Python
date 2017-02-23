"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substrin
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        pt_i = pt_e = 0
        maxlen = 1
        count = 0
        letterdict = {}
        pt_start = pt_end = 0
        for pt_e in xrange(len(s)):
            if not letterdict.has_key(s[pt_e]) or letterdict[s[pt_e]] == 0:
                letterdict[s[pt_e]] = 1
                count += 1
            elif letterdict[s[pt_e]] > 0: # repeating letter encountered
                if count > maxlen:
                    maxlen = count
                    pt_start, pt_end = pt_i, pt_e
                while s[pt_i] != s[pt_e]:
                    letterdict[s[pt_i]]  = 0
                    count -= 1
                    pt_i += 1
                pt_i += 1
        return max(maxlen, count)