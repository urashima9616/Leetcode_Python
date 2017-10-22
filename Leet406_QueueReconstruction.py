class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def queueReconstruction(people):
    people = sorted(people, key = lambda x: x[0])
    new_people = [ (-1,-1) for _ in xrange(len(people))]
    head = None
    i = len(people) - 1
    while i >= 0:
        j = i 
        while j >0 and people[j-1][0] == people[i][0]:
            j -= 1
        for k in xrange(j, i+1):
            cnt = people[k][1]
            node = Node(people[k])
            pt = head
            if head == None:
                head = node
                continue
            while cnt > 1:
                pt = pt.next
                cnt -= 1
            else:
                if cnt == 0:
                    node.next = head
                    head = node
                else:
                    node.next, pt.next = pt.next, node
        i = j-1
    res = []
    pt = head
    while pt:
        res.append(pt.val)
        pt = pt.next
    return res
                

  




print queueReconstruction([[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]])
        
        




