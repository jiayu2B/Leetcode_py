class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left+right)/2
            
            if nums[mid] == target:
                return mid
            #二分搜索必须要在有序数列上，所以第一是先判断是前半段还是后半段有序。
            #判断有序后，看target是否在该数列中。在的话就二分搜索这一段。不在的话就重新对另一端进行操作。
            if nums[mid] < nums[right]:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                
                    
