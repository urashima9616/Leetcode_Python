def longestReplacement(s,k):
    """
    type s: string
    rtype: int
    """
    opt = [[ [0, 0] for i in xrange(k+1)] for j in xrange(len(s))]
    penalty_mat = [[-1 for i in xrange(len(s))] for j in xrange(len(s))]


    for j in xrange(k+1):
        opt[0][j] = [j, 1]

    for i in xrange(1, len(s)):
        opt[i][k] = [opt[i-1][k][0], 1 + opt[i-1][k]] if s[i] == s[i-1] else [s[i], 1]
    res = 0
    
    for i in xrange(1, len(s)):
        for j in reversed(xrange(1, k)):
            if s[i] == s[i-1]:
                opt[i][j] = opt[i-1][j] + 1
            else:
                max_cur = 0
                for t in xrange(i):
                    if penalty_mat[t][i] != -1:
                        penalty = penalty_mat[t][i]
                    else:
                        pt = t
                        penalty  = 0
                        while pt <= i:
                            if s[pt] != s[t]:
                                penalty += 1
                            pt += 1
                    penalty_mat[t][i] = penalty
                    if penalty + j > k:
                        continue
                    else:
                        if max_cur < opt[t][j+penalty] + i - t:
                            max_cur = opt[t][j+penalty] + i - t
                opt[i][j] = max_cur 
            if res < opt[i][j]:
                res = opt[i][j]
    return res

print longestReplacement("AABBAA", 2)
                  


                    


