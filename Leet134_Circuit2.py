"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Idea: 
start at 0 onwards, if you run out of gas at i-th, 
it means no matter where you start from [0, i-1], you are bound to run of gas
why ? because you must start from a node where you have more gas than cost.
So if you start at 1, let say, the accumulative gain at i is less than you start at 0,
therefore there is no need to check any node between [start, i]
so you will check i+1 onwards

The code below is valid only there is unique solution
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        gas_sum = 0
        cost_sum = 0
        for i in xrange(len(gas)-1):
            gas_sum  += gas[i]
            cost_sum += cost[i]
            if tank + gas[i] < cost[i]:
                tank = 0
                start = i+1
            else:
                tank = gas[i] - cost[i] + tank
        #Here the idea is:
        #Since you arrived at i-1 => you have non-zero tank
        #
        gas_sum += gas[-1]
        cost_sum += cost[-1]
        if gas_sum < cost_sum:
            return -1
        else:
            return start
        
                
            
            

        