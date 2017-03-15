# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        pt = RandomListNode(head.label)
        head2 = pt
        pt2 = head
        label_dict = {}
        label_dict[pt.label] = pt 
        while pt and pt2:
            #Check random
            if pt2.random:
                pt.random = label_dict[pt2.random.label] if label_dict.has_key(pt2.random.label) else RandomListNode(pt2.random.label)
                if not label_dict.has_key(pt2.random.label):
                    label_dict[pt2.random.label] = pt.random
                #label_dict[pt2.random.label] = pt.random if not label_dict.has_key(pt2.random.label)
            if pt2.next:
                pt.next = label_dict[pt2.next.label] if label_dict.has_key(pt2.next.label) else RandomListNode(pt2.next.label)
                if not label_dict.has_key(pt2.next.label):
                    label_dict[pt2.next.label] = pt.next 
            pt = pt.next
            pt2 = pt2.next
        return head2



            
            
                    
                
            
            
            