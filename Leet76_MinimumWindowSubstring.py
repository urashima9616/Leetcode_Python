"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
Idea: 
You restart the counting only when you are short of required letters
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        missdict = {}
        p1 = p2 = 0
        count = tlen = len(t)
        minlen = len(s) + 1
        pstart = 0
        pend = 0
        for each in t:
            if missdict.has_key(each):
                missdict[each] += 1
            else:
                missdict[each] = 1
        for p2 in xrange(len(s)):
            if missdict.has_key(s[p2]):
                if missdict[s[p2]] > 0:
                    count -= 1
                missdict[s[p2]] -= 1
            while count == 0:
                #valid, update len
                cur_len = p2 - p1 + 1
                if cur_len < minlen:
                    minlen = cur_len
                    pstart, pend = p1, p2
                if missdict.has_key(s[p1]) and missdict[s[p1]] == 0:
                    #You restart the counting only when you are short of required letters
                    count += 1
                if missdict.has_key(s[p1]):
                    missdict[s[p1]] += 1
                p1 += 1
                    
        if minlen == len(s) + 1:
            return ""
        return s[pstart:pend+1]
Solve = Solution()
Solve.minWindow("AAAADOBECODEBANC", "ADB" )