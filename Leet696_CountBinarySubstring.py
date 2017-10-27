class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        prefix = None
        num = 0
        i = 0
        while i< len(s):
            prefix = s[i]
            cnt = 1
            state = s[i]
            length = 1
            for j in xrange(i+1, len(s)):
                if s[j] == prefix and state == s[i] and j != len(s) - 1:
                    cnt += 1
                elif s[j] == prefix and state == s[i] and j == len(s) - 1:
                    cnt += 1
                    length = cnt
                    break
                elif s[j] != prefix and state == s[i]:
                    length = cnt
                    cnt -= 1 
                    state = s[j]
                elif state != s[i] and s[j] == prefix:
                    break
                else:
                    cnt -= 1
                if cnt == 0:
                    break
            if cnt == length:
                return num
            num += length - cnt
            i += length
        return num
solve = Solution()
print solve.countBinarySubstrings("00")