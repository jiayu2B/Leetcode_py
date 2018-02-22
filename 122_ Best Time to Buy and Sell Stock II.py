class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_pro = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                max_pro+= prices[i] - prices[i-1]
        return max_pro
