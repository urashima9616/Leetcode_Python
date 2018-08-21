import collections, Queue
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        task_load = Queue.PriorityQueue()
        block = 0
        schedule = []
        choice = set()
        for (key, value) in cnt.items():
            task_load.put((-value, key))
            choice.add(key)
        while len(cnt) > 0:
            pt = 0
            while not task_load.empty() and pt < n+1:
                count, next_task = task_load.get()
                schedule.append(next_task)
                choice.remove(next_task)
                cnt[next_task] -=1
                if cnt[next_task] == 0:
                    cnt.pop(next_task)
                pt += 1
            else:
                if task_load.empty():
                    while pt < n+1:
                        schedule.append("idle")
                        pt += 1
                for (key, value) in cnt.items():
                    if key not in choice:
                        task_load.put((-value, key))
                        choice.add(key)
        return schedule
solve = Solution()
print solve.leastInterval(["A","A","A","A","A","A","B","B", "C","D","E","F","G", "G","G"], 2)