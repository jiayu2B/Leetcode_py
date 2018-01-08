class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        G = nums[0]
        #使用穷举法，穷举出G能够达到的最大值
        for i in range(1,len(nums)):
            #当G小于i的时候，代表G达不到i，因此返回False
            if G < i:
                return False
            G = max(G, nums[i]+i)
            
        return G >= len(nums)-1
        
        
