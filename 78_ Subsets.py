class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS(nums, [], 0)
        return self.res
    def DFS(self, nums, _list, _start):
        self.res.append(_list[:])
        
        for i in range(_start, len(nums)):
            _list.append(nums[i])
            self.DFS(nums, _list, i+1)
            _list.remove(nums[i])
    #使用DFS算法，找子集
