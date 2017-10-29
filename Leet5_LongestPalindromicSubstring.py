class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        opt = [[0 for i in xrange(len(s))] for j in xrange(len(s))]
        max_len = 1
        max_idx = [0,0]
        for i in xrange(len(s)):
            opt[i][i] = 1
        for i in xrange(len(s)-1):
            if s[i] == s[i+1]:
                opt[i][i+1] = 2
                if opt[i][i+1] > max_len:
                        max_len = opt[i][i+1]
                        max_idx = [i, i+1]
        #fill the entry with gap%2 == 0
        for i in xrange(len(s)-1):
            k = i-1
            j = i+1
            while k >= 0 and j< len(s):
                if s[k] == s[j]:
                    opt[k][j] = opt[k+1][j-1] + 2
                    if opt[k][j] > max_len:
                        max_len = opt[k][j]
                        max_idx = [k, j]
                    k -= 1
                    j += 1
                else:
                    break
            if s[i] == s[i+1]:
                k = i-1
                j = i+2
                while k >= 0 and j < len(s):
                    if s[k] == s[j]:
                        opt[k][j] = opt[k+1][j-1] + 2
                        if opt[k][j] > max_len:
                            max_len = opt[k][j]
                            max_idx = [k, j]
                        k -= 1
                        j += 1
                    else:
                        break
        return s[max_idx[0]:max_idx[1]+1]
