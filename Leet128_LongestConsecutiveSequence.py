"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Key idea: 
将序列中的所有数存到一个unordered_set中。
对于序列里任意一个数A[i]，
我们可以通过set马上能知道A[i]+1和A[i]-1是否也在序列中。
如果在，继续找A[i]+2和A[i]-2，
以此类推，直到将整个连续序列找到。
为了避免在扫描到A[i]-1时再次重复搜索该序列，
在从每次搜索的同时将搜索到的数从set中删除。
直到set中为空时，所有连续序列搜索结束。
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        consec_set = set()
        while num_set:
            each = num_set.pop()
            consec_set.clear()
            consec_set.add(each)
            temp_pos = each+1
            temp_neg = each-1
            #forward search
            while temp_pos in num_set or temp_neg in num_set:
                if temp_pos in num_set:
                    consec_set.add(temp_pos)
                    num_set.discard(temp_pos)
                    temp_pos += 1
                if temp_neg in num_set:
                    consec_set.add(temp_neg)
                    num_set.discard(temp_neg)
                    temp_neg -= 1
            if max_len < len(consec_set):
                max_len = len(consec_set)
        return max_len