class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            tem = target - nums[i]
            j = self.bis(nums, tem, i+1)
            if j > -1:
                return [i+1, j+1]
    #二分查找
    def bis(self, nums, tem, start):
        left = start
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] < tem:
                left = mid +1
            elif nums[mid] > tem:
                right = mid - 1
            else:
                return mid
        return -1
            
    
