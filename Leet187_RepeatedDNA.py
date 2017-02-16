class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        slice_len = 10
        if not s:
            return []
        s_len = len(s)
        if s_len < slice_len:
            return []
        
        start = 0
        end  = slice_len
        sub_dict = {}
        res = []
        while end <= s_len:
            if not sub_dict.has_key(s[start:end]):
                sub_dict[s[start:end]] = 1
            else:
                sub_dict[s[start:end]] += 1
            start += 1
            end += 1
        for key, val in sub_dict.items():
            if val > 1:
                res.append(key)
        return res