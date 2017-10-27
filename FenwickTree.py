class FenwickTree(object):
    def __init__(self,array):
        self.nums = [0 for _ in xrange(len(array))]
        self.size = len(array)
        for pos in xrange(self.size):
            self.update(pos, array[pos])

    def update(self, idx, val): # 1011, 1100, 10000, ..., size of array
        pos = idx + 1
        while pos <= self.size:
            self.nums[pos-1] += val
            pos += pos & (-pos)
    def get(self, idx): # 1011, 1010, 1000, 0000
        pos = idx + 1
        temp = 0
        while pos > 0:
            temp += self.nums[pos-1]
            pos -= pos & (-pos)
        return temp

nums = [ 1,2,3,4,5,6]
bit = FenwickTree(nums)
print bit.get(0)

            
