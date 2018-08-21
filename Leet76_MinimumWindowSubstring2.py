import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #opt represents the minimal length of the window that contains T
        left, right = [0]*2
        need_dict = collections.Counter(t)
        symbol_dict =  collections.Counter(t)
        min_len = len(s)+1
        min_i, min_j = 0,0
        while 1:
            while right < len(s):
                if s[right] in need_dict:
                    if s[right] in symbol_dict:
                        symbol_dict[s[right]] -= 1
                        if symbol_dict[s[right]] == 0:
                            symbol_dict.pop(s[right])
                    need_dict[s[right]] -= 1
                    
                    if len(symbol_dict) == 0:
                        break
                right += 1
            if right == len(s) and len(symbol_dict) > 0:
                return s[min_i:min_j]
            while left < right:
                if s[left] in need_dict and need_dict[s[left]] < 0:
                    need_dict[s[left]] += 1
                    left += 1
                elif s[left] not in need_dict:
                    left += 1
                elif s[left] in need_dict and need_dict[s[left]] == 0:
                    break
            if right - left < min_len:
                min_len = right-left
                min_i, min_j = left, right
            symbol_dict[s[left]] = 1
            need_dict[s[left]] += 1
            left += 1
            if right == len(s) -1:
                break
        return s[min_i:min_j]
Solve = Solution()
Solve.minWindow("ADOBECODEBANC", "ABC")