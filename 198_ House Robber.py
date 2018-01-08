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
        lis = [0 for i in range(len(nums))]
        lis[0] = nums[0]
        lis[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            lis[i] = max(lis[i-1],lis[i-2]+nums[i])
            #设定好lis[1],lis[0].然后从lis[2]开始进行规划。看是lis[0]+nums[2]大还是lis[1]大
        return lis[-1]
