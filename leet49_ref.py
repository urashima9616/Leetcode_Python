import sys,os
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        length_str = len(strs)
        word_dict = {}
        res = []
        index_word = 0
        for each in strs:
            work_list = list(each)
            work_list.sort()
            str_key = ''.join(work_list)
            index = word_dict.get(str_key)
            if index != None:
                res[index].append(each)
            else:
                word_dict[str_key] = index_word
                res.append([each])
                index_word += 1
        return res
        
        
                



        


my_solution = Solution()
print my_solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        
      