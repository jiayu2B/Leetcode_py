class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in range(1,len(nums)):
            res.append(res[-1]*nums[i-1])
        #每一个数字乘他之前所有数
        product = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * product
            product = product * nums[i]
        #每一个数组乘他之后所有数
        return res
