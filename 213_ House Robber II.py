class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums)== 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        #由于第一个和最后一个不能同时选，将问题分解成两个，一个是从第一个到倒数第二个，一个是从第二个到倒数第一个
        a = self.rob_(nums[0:len(nums)-1])
        b = self.rob_(nums[1:len(nums)])
        return max(a,b)
        
    def rob_(self, nums):
        lis = [0 for i in range(len(nums))]
        lis[0] = nums[0]
        lis[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            lis[i] = max(lis[i-1],lis[i-2]+nums[i])
        return lis[-1]
