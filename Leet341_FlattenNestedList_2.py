class ListIterator(object):

    def __init__(self, nums):
        self.stack = [nums]
    def __iter__(self):
        return self
    def hasNext(self):
        return self.stack.count > 0

    def next(self):
        #type nums: List[List]
        #rtype : List[int]
        while self.stack.count > 0:
            cur = self.stack.pop()
            if not isinstance(cur, list):
                return cur
            else:
                for i in xrange(len(cur)):
                    if not isinstance(cur[i],list):
                        return cur[i]
                    else:
                        self.stack.append(cur[i+1:])
                        self.stack.append(cur[i])
                        break
it = ListIterator([1,2,3,[4,[5,6],7]])

while it.hasNext():
    print it.next()

                

    