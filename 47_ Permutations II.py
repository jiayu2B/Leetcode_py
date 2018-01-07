class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        flaglist = [0]*len(nums)
        #设置一个flag表
        nums.sort()
        self.DFS(nums, [], flaglist)
        return self.res
    
    def DFS(self, nums, _list, flag):
        if len(_list)==len(nums):
            self.res.append(_list[:])
            return
        last = None
        #定义一个last数字，防止重复数字
        for i in range(0,len(nums)):
            if flag[i] == 1:
                continue
            if last == nums[i]:
                continue
            flag[i] = 1
            _list.append(nums[i])
            self.DFS(nums, _list, flag)
            last = _list.pop()
            flag[i] = 0
