class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sumcost = 0
        total = 0
        min_idx = 0
        #基本逻辑1： 只要total大于0就可以环绕
        #基本逻辑2： 设置一个sumcost，如果sumcost加上本地的油不能支付下一航程，则index为下一段开始。如果可以，则加上下一段航程的消耗
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if sumcost + gas[i] < cost[i]:
                sumcost = 0 
                min_idx = i + 1
            else:
                sumcost += gas[i] - cost[i]
        if total >= 0:
            return min_idx
        else:
            return -1
