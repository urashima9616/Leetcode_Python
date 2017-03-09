"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


The DP idea works like this:
let us say we know the optimal solution all the way to i-1 step
then here comes the i-th element, then the optimal solution for i-th step
must be obtained by following situations:
i-th element reaches back to certain elment j and construct a palindrome
the cut number is opt[j] + 1

then the optimal soution is the minimum of all possible such reaches.
that is to say, min(opt[j]+1) for all j<=i and P[i,j] == 1
<opt[j]<---------i
==================

#The calculation of P[i,j]


"""