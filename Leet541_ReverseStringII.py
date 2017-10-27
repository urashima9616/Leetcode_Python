class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        new_s = ""
        num_units = len(s)/(2*k)
        num_residual = len(s)%(2*k)
        for i in xrange(num_units+1):
            if i < num_units:
                new_s += s[i*2*k:i*2*k+k][::-1] + s[i*2*k+k : (i+1)*2*k]
            else:
                if num_residual < k:
                    new_s += s[i*2*k:]
                else:
                    new_s += s[i*2*k:i*2*k+k][::-1] + s[i*2*k+k:]
        return new_s
solve = Solution()
print solve.reverseStr("abcdefg", 2)