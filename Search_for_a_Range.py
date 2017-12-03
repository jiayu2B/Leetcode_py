class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = [-1,-1]
        left = 0; right = len(nums) - 1 
        flag = 0
        while (left <= right) :
            mid = (left + right)/2
            if nums[mid] == target:
                left,right = mid,mid
                flag = 1
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        
        if flag == 0: return arr
        
        while left > 0:
            if nums[left-1] != target:
                break
            left -= 1
        while right < len(nums) - 1:
            if nums[right+1] != target:
                break
            right += 1
        arr = [left,right]
        return arr
