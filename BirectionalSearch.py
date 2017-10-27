class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        fw_set = set([word1])
        bw_set = set([word2])
        fw, bw = (1,0)
        fw_child = [word1]
        bw_child = [word2]
        fw_dict = {}
        bw_dict = {}
        fw_cnt = 0
        bw_cnt = 0
        while len(fw_set & bw_set) == 0:
            if fw == 1:
                next_child = []
                for each in fw_child:
                    for i in xrange(len(each)):
                        next_child.append(each[:i] + each[i+1:])
                        fw_set.add(each[:i] + each[i+1:])
                        if each[:i] + each[i+1:] not in fw_dict:
                            fw_dict[each[:i] + each[i+1:]] = fw_cnt +1
                fw_child = next_child
                fw_cnt += 1
 
            else:
                next_child = []
                for each in bw_child:
                    for i in xrange(len(each)):
                        next_child.append(each[:i] + each[i+1:])
                        bw_set.add(each[:i] + each[i+1:])
                        if each[:i] + each[i+1:] not in bw_dict:
                            bw_dict[each[:i] + each[i+1:]] = bw_cnt +1
                bw_child = next_child
                bw_cnt +=1
            fw, bw = bw, fw
        else: 
            min_step = len(word1) + len(word2)
            for each in (fw_set & bw_set):
                if fw_dict[each] + bw_dict[each] < min_step:
                    min_step = fw_dict[each] + bw_dict[each]
            
                
            
        return min_step
            
                
                
                
        