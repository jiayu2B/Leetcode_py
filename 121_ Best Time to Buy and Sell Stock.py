class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        res = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            buy = min(buy, prices[i])
            res = max(res, prices[i] - buy)
        return res
