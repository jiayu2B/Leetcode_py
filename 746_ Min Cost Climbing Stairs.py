class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <2:
            return min(cost)
        dp = [cost[0],cost[1]]
        for i in range(2,len(cost)):
            dp.append(min( dp[i-2] + cost[i], dp[i-1] + cost[i]))
        return min(dp[-1], dp[-2])
