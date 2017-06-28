"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        self.count = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            entry = self.cache.pop(key)
            self.cache[key] = entry
            return entry
        else:
            return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if self.count < self.capacity:
                self.cache[key] = value
                self.count += 1
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)