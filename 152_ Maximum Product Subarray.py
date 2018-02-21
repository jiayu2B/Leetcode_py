class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #需要设定min,max，为了防止从负数一下到正数
        ans = max_ = min_ = nums[0]
        for i in range(1, len(nums)):
            #设定两个tem参数，max和min在tem， num[i]中选。
            tem1, tem2 = max_*nums[i], min_*nums[i]
            max_ = max( max(tem1, tem2), nums[i])
            min_ = min( min(tem1, tem2), nums[i])
            ans = max(max_, ans)
        return ans
