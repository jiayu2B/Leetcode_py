class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res^=i
        return res
        #利用位运算的特性，不同位取1，导致res成为独立的那个数字
