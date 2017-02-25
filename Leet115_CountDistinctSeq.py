"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
Total Accepted: 65338
Total Submissions: 211974
Difficulty: Hard
Contributors: Admin
State transition equation:
if T[i] = S[j]:
    the # of distinct subsequence is sum of two parts :
    1. op[i-1][j-1](formed by matched subsequnce in S[j-1] + 'T[i]')
    2. op[i][j-1] (formed by matched subsequence in S[j-1] replacing old 'T[i]' with T[i] )
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        op_matrix = [[0 for i in xrange(len(s)+1)] for j in xrange(len(t)+1)]
        for i in xrange(len(t)+1):
            for j in xrange(len(s)+1):
                if i == 0:
                    op_matrix[i][j] = 1
                    continue
                if j == 0 and i != 0: 
                    op_matrix[i][j] = 0
                    continue
                if s[j-1] == t[i-1]:
                    op_matrix[i][j] = op_matrix[i-1][j-1] + op_matrix[i][j-1]
                else:
                    op_matrix[i][j] = op_matrix[i][j-1]
        return op_matrix[len(t)][len(s)]
Solve = Solution()
Solve.numDistinct("rabbbit", "rabbit")