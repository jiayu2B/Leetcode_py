class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 2: return nums
        max_t = [self.maxfind(nums,0,k)]
        for i in range(0,len(nums)-k):
        #三个限制，如果新来的数比之前的大，就用新来的。如果出去的数就是最大数，name计算一次。如果都不是，那就还是原来的
            if nums[i+k] >= max_t[-1]:
                max_t.append(nums[i+k])
            elif nums[i] == max_t[-1]:
                max_t.append(self.maxfind(nums,i+1,k))
            else:
                max_t.append(max_t[-1])
        return max_t
                
    def maxfind(self, nums, i, k):
        return max(nums[i:i+k])
